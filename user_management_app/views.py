from django.contrib.auth import authenticate, login
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile
from PIL import Image
from io import BytesIO
import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Create your views here.
class UserSignUpView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        # Validate required fields
        if not username or not email or not password or not confirm_password:
            return Response({'error': 'Please provide all the fields.'}, status=400)

        # check email valid or not
        if not is_valid_email(email):
            return Response({'error': 'Please enter valid email.'}, status=400)

        # check length of password
        if len(password) < 6:
            return Response({'error': 'password must be 6 character'}, status=400)

        # check password and confirm password same or not
        if password != confirm_password:
            return Response({'error': 'password and confirm_password not same'}, status=400)

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already exist.'}, status=400)

        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return Response({
            'success': 'User created successfully.',
            'user_id': user.pk
            }, status=201)


class UserLoginView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')

        # required all fields
        if not username or not password:
            return Response({'error': 'Please provide both username and password.'}, status=400)

        # check Authenticate user
        user = authenticate(request, username=username, password=password)

        # Check authentication user or not
        if user is None:
            return Response({'error': 'Invalid username or password.'}, status=401)

        # Log in the user
        login(request, user)

        return Response({
            'success': 'User logged in successfully.',
            'user_id': user.pk
        }, status=200)


class UserProfileView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):

        user_id = request.data.get('user_id')
        profile_photo = request.FILES.get('profile_photo')
        location = request.data.get('location')
        designation = request.data.get('designation')

        # Validate required fields
        if not user_id:
            return Response({'error': 'Please provide user_id fields.'}, status=400)

        # get user record and check exist or not
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "enter user_id record not found"})

        print("Orignal image size", profile_photo.size)

        if profile_photo:
            # Check the photo size
            if profile_photo.size > 1024 * 1024:

                # Compress the photo
                compressed_photo = self.compress_photo(profile_photo)
                print()
                print("compressed photho", compressed_photo)
                if not compressed_photo:
                    return Response({'error': 'Failed to compress photo'}, status=400)

                profile_photo = compressed_photo
            else:
                profile_photo = profile_photo

        print()
        print("After Compress image size", profile_photo.size)
        #  create the profile
        create_profile = Profile.objects.create(user=user, photo=profile_photo, location=location, designation=designation)
        create_profile.save()
        
        return Response({"success": "Profile create successfully"})

    
    def compress_photo(self, photo):
        try:
            # Open the image using PIL
            image = Image.open(photo)

            # Create a BytesIO object to hold the compressed image data
            compressed_image_io = BytesIO()

            # Check the image format and convert it to JPEG if needed
            if image.format != 'JPEG':
                image = image.convert('RGB')

            # Compress the image and save it to the BytesIO object
            image.save(compressed_image_io, format='JPEG', optimize=True, quality=60)

            # Create a new InMemoryUploadedFile with the compressed image data
            compressed_photo = InMemoryUploadedFile(
                compressed_image_io,
                None,
                photo.name,
                'image/jpeg',
                compressed_image_io.tell,
                None
            )

            return compressed_photo
        except Exception as e:
            # Handle any errors that occur during compression
            print(f"Compression error: {e}")
            return None



