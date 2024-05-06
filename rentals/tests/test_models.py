from django.test import TestCase
from rentals.models import (
    CarType, CarModel, ShopInfo, SocialHandle, ServiceReview,
    )
from django.core.files.uploadedfile import SimpleUploadedFile
import os


# Create your tests here. Write, call it once and pass it 
# TEST THE MODELS
class ModelTestCase(TestCase):
    # create a setUp to store model instance in a class-level variable
    # to make it accessible to all test methods within the test case
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.image_path = 'media/defender.jpg'
        
        with open(cls.image_path, 'rb') as file:
            cls.image_data = file.read()
            
        cls.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=cls.image_data,
            content_type='image/jpeg',
            )

        # car type instance
        cls.car_type_instance = CarType.objects.create(
            type_image = cls.test_image,
            type_name = "Mytype",
            description = "An exotic car type",
            is_available = True
        )
        
        # car model instance
        cls.car_model_instance = CarModel.objects.create(
            type = cls.car_type_instance,
            brand_name = "Jjodem",
            model_name = "Jjodem Rentals",
            model_image = cls.test_image,
            number_of_doors = 4,
            number_of_passengers = 4,
            fuel = "Gasoline",
            transmission = "Automatic",
            drive_type = "4WD",
            description = "Jjodem rental type",
            is_available = True,
            price = 750,
        )
        
        
    def tearDown(self): # delete temp file
        if self.car_type_instance.type_image:
            os.remove(self.car_type_instance.type_image.path)
        if self.car_model_instance.model_image:
            os.remove(self.car_model_instance.model_image.path)
            
    
    # TEST FOR CarType MODEL
    '''
    TEST:
        # if the imagefield contains the image
        # the number of instances created
        # if the path of the image field matches the path of the original jpg file
        # if the str() function returns the model name as specified in the model
        # if the test instance is the same as the CarModel
    '''
    def test_model_CarType(self):
        # Retrieve saved instance from database
        # saved_car_type_instance = CarType.objects.get(id=self.car_type_instance.id)
        saved_car_type_instance = ModelTestCase.car_type_instance
        
        self.assertIsNotNone(saved_car_type_instance.type_image)
        self.assertEqual(CarType.objects.count(), 1)
        self.assertEqual(saved_car_type_instance.type_image, 'type_upload/test_image.jpg')
        self.assertEquals(str(saved_car_type_instance), "Mytype")
        self.assertTrue(isinstance(saved_car_type_instance, CarType))
        
        max_length = saved_car_type_instance._meta.get_field('type_name').max_length
        self.assertEqual(max_length, 100)

    
    # TEST FOR CarModel MODEL  
    # def test_model_CarModel(self):
    #     # Retrieve saved instance from database
    #     saved_car_model_instance = CarModel.objects.get(pk=self.car_model_instance.pk)
        
    #     self.assertIsNotNone(saved_car_model_instance.model_image)
    #     self.assertEqual(CarModel.objects.count(), 1)
    #     self.assertEqual(saved_car_model_instance.model_image, 'model_upload/test_image.jpg')
    #     self.assertEquals(str(saved_car_model_instance), "Jjodem Rentals")
    #     self.assertTrue(isinstance(saved_car_model_instance, CarModel))

    