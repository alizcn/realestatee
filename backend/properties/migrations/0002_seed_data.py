# Generated manually - Seed data for properties

from django.db import migrations
from django.utils import timezone
from datetime import timedelta
import random


def create_mock_data(apps, schema_editor):
    Property = apps.get_model('properties', 'Property')
    Inquiry = apps.get_model('properties', 'Inquiry')

    # Mock Properties
    properties_data = [
        {
            'title': 'Modern Loft in City Center',
            'description': 'Stunning modern loft with floor-to-ceiling windows, exposed brick walls, and premium finishes. Open concept living space with chef\'s kitchen featuring stainless steel appliances. Walking distance to restaurants, shops, and public transit.',
            'property_type': 'apartment',
            'address': '123 Main Street, Apt 4B',
            'city': 'Istanbul',
            'state': 'Marmara',
            'zip_code': '34000',
            'price': 2500000.00,
            'bedrooms': 2,
            'bathrooms': 2.0,
            'area_sqft': 1200,
            'image_url': 'https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800',
            'agent_name': 'Ahmet Yilmaz',
            'agent_phone': '+90 532 123 4567',
            'agent_email': 'ahmet.yilmaz@realestate.com',
            'status': 'available',
        },
        {
            'title': 'Spacious Family Villa with Garden',
            'description': 'Beautiful 4-bedroom villa in a quiet neighborhood. Features a large backyard with swimming pool, modern kitchen, spacious living areas, and a two-car garage. Perfect for families looking for comfort and space.',
            'property_type': 'villa',
            'address': '456 Oak Avenue',
            'city': 'Ankara',
            'state': 'Ic Anadolu',
            'zip_code': '06000',
            'price': 4500000.00,
            'bedrooms': 4,
            'bathrooms': 3.5,
            'area_sqft': 3200,
            'image_url': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=800',
            'agent_name': 'Elif Demir',
            'agent_phone': '+90 533 234 5678',
            'agent_email': 'elif.demir@realestate.com',
            'status': 'available',
        },
        {
            'title': 'Cozy Studio Near University',
            'description': 'Perfect starter home or investment property. This cozy studio features efficient use of space, modern appliances, and is located near major universities and public transportation. Ideal for students or young professionals.',
            'property_type': 'apartment',
            'address': '789 College Road, Unit 12',
            'city': 'Izmir',
            'state': 'Ege',
            'zip_code': '35000',
            'price': 850000.00,
            'bedrooms': 1,
            'bathrooms': 1.0,
            'area_sqft': 450,
            'image_url': 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800',
            'agent_name': 'Mehmet Kaya',
            'agent_phone': '+90 534 345 6789',
            'agent_email': 'mehmet.kaya@realestate.com',
            'status': 'available',
        },
        {
            'title': 'Luxury Penthouse with Sea View',
            'description': 'Exclusive penthouse offering breathtaking panoramic sea views. Features include private elevator access, rooftop terrace, smart home technology, and premium finishes throughout. The ultimate in luxury living.',
            'property_type': 'condo',
            'address': '1000 Seaside Boulevard, PH1',
            'city': 'Antalya',
            'state': 'Akdeniz',
            'zip_code': '07000',
            'price': 8500000.00,
            'bedrooms': 3,
            'bathrooms': 3.0,
            'area_sqft': 2800,
            'image_url': 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800',
            'agent_name': 'Zeynep Ozturk',
            'agent_phone': '+90 535 456 7890',
            'agent_email': 'zeynep.ozturk@realestate.com',
            'status': 'pending',
        },
        {
            'title': 'Charming Traditional House',
            'description': 'Beautifully restored traditional house with original architectural details. Features include wooden beams, courtyard garden, updated kitchen and bathrooms while maintaining historic charm. A rare find!',
            'property_type': 'house',
            'address': '25 Heritage Lane',
            'city': 'Bursa',
            'state': 'Marmara',
            'zip_code': '16000',
            'price': 3200000.00,
            'bedrooms': 3,
            'bathrooms': 2.0,
            'area_sqft': 1800,
            'image_url': 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=800',
            'agent_name': 'Can Arslan',
            'agent_phone': '+90 536 567 8901',
            'agent_email': 'can.arslan@realestate.com',
            'status': 'available',
        },
        {
            'title': 'Modern Smart Home',
            'description': 'State-of-the-art smart home with integrated home automation system. Control lighting, climate, security, and entertainment from your phone. Energy-efficient design with solar panels and modern aesthetics.',
            'property_type': 'house',
            'address': '88 Innovation Drive',
            'city': 'Istanbul',
            'state': 'Marmara',
            'zip_code': '34100',
            'price': 5800000.00,
            'bedrooms': 4,
            'bathrooms': 3.0,
            'area_sqft': 2600,
            'image_url': 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800',
            'agent_name': 'Ahmet Yilmaz',
            'agent_phone': '+90 532 123 4567',
            'agent_email': 'ahmet.yilmaz@realestate.com',
            'status': 'available',
        },
        {
            'title': 'Downtown Business District Condo',
            'description': 'Prime location in the heart of the business district. This sleek condo offers modern living with easy access to offices, restaurants, and nightlife. Building amenities include gym, pool, and 24/7 concierge.',
            'property_type': 'condo',
            'address': '500 Business Center, Unit 1205',
            'city': 'Istanbul',
            'state': 'Marmara',
            'zip_code': '34200',
            'price': 3100000.00,
            'bedrooms': 2,
            'bathrooms': 2.0,
            'area_sqft': 1100,
            'image_url': 'https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800',
            'agent_name': 'Elif Demir',
            'agent_phone': '+90 533 234 5678',
            'agent_email': 'elif.demir@realestate.com',
            'status': 'available',
        },
        {
            'title': 'Beachfront Summer House',
            'description': 'Escape to this beautiful beachfront property. Direct beach access, outdoor dining area, hammock garden, and stunning sunset views. Perfect as a vacation home or rental investment property.',
            'property_type': 'house',
            'address': '15 Coastal Highway',
            'city': 'Bodrum',
            'state': 'Ege',
            'zip_code': '48400',
            'price': 6200000.00,
            'bedrooms': 3,
            'bathrooms': 2.5,
            'area_sqft': 1900,
            'image_url': 'https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?w=800',
            'agent_name': 'Zeynep Ozturk',
            'agent_phone': '+90 535 456 7890',
            'agent_email': 'zeynep.ozturk@realestate.com',
            'status': 'sold',
        },
        {
            'title': 'Affordable Family Apartment',
            'description': 'Well-maintained apartment in a family-friendly neighborhood. Close to schools, parks, and shopping centers. Features include balcony, storage room, and parking space. Great value for growing families.',
            'property_type': 'apartment',
            'address': '200 Family Street, Apt 3A',
            'city': 'Kayseri',
            'state': 'Ic Anadolu',
            'zip_code': '38000',
            'price': 1200000.00,
            'bedrooms': 3,
            'bathrooms': 1.5,
            'area_sqft': 1350,
            'image_url': 'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=800',
            'agent_name': 'Mehmet Kaya',
            'agent_phone': '+90 534 345 6789',
            'agent_email': 'mehmet.kaya@realestate.com',
            'status': 'available',
        },
        {
            'title': 'Mountain View Retreat',
            'description': 'Peaceful retreat with stunning mountain views. This property offers privacy, nature, and tranquility. Features include fireplace, large deck, hiking trails access, and organic garden space.',
            'property_type': 'villa',
            'address': '5 Mountain Road',
            'city': 'Bolu',
            'state': 'Karadeniz',
            'zip_code': '14000',
            'price': 2800000.00,
            'bedrooms': 4,
            'bathrooms': 2.5,
            'area_sqft': 2200,
            'image_url': 'https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=800',
            'agent_name': 'Can Arslan',
            'agent_phone': '+90 536 567 8901',
            'agent_email': 'can.arslan@realestate.com',
            'status': 'available',
        },
    ]

    # Create properties with varying listed_at dates
    created_properties = []
    base_date = timezone.now()

    for i, prop_data in enumerate(properties_data):
        prop_data['listed_at'] = base_date - timedelta(days=i * 7)
        prop = Property.objects.create(**prop_data)
        created_properties.append(prop)

    # Mock Inquiries
    inquiries_data = [
        {
            'property': created_properties[0],
            'name': 'Fatma Celik',
            'email': 'fatma.celik@email.com',
            'phone': '+90 537 111 2233',
            'message': 'I am very interested in this property. Is it possible to schedule a viewing this weekend? I would also like to know if the price is negotiable.',
        },
        {
            'property': created_properties[0],
            'name': 'Burak Sahin',
            'email': 'burak.sahin@email.com',
            'phone': '+90 538 222 3344',
            'message': 'Could you please provide more details about the building amenities and monthly maintenance fees?',
        },
        {
            'property': created_properties[1],
            'name': 'Ayse Yildiz',
            'email': 'ayse.yildiz@email.com',
            'phone': '+90 539 333 4455',
            'message': 'This villa looks perfect for my family. Is the swimming pool heated? Also, what is the condition of the garden?',
        },
        {
            'property': created_properties[3],
            'name': 'Kemal Erdogan',
            'email': 'kemal.erdogan@email.com',
            'phone': '+90 540 444 5566',
            'message': 'I would like to make an offer on this penthouse. Please contact me at your earliest convenience to discuss the terms.',
        },
        {
            'property': created_properties[4],
            'name': 'Selin Aktas',
            'email': 'selin.aktas@email.com',
            'phone': '',
            'message': 'I love traditional architecture. Can you tell me more about the restoration work that was done? Are there any photos of the courtyard?',
        },
        {
            'property': created_properties[5],
            'name': 'Ozan Polat',
            'email': 'ozan.polat@email.com',
            'phone': '+90 541 555 6677',
            'message': 'As a tech enthusiast, I am very interested in the smart home features. What systems are installed and are they compatible with popular platforms?',
        },
        {
            'property': created_properties[6],
            'name': 'Deniz Korkmaz',
            'email': 'deniz.korkmaz@email.com',
            'phone': '+90 542 666 7788',
            'message': 'I work in the business district and this location is perfect. What are the HOA fees and what do they include?',
        },
        {
            'property': created_properties[9],
            'name': 'Emre Tas',
            'email': 'emre.tas@email.com',
            'phone': '+90 543 777 8899',
            'message': 'Looking for a peaceful retreat from city life. Is this property accessible year-round? What are the winters like in this area?',
        },
    ]

    # Create inquiries with varying created_at dates
    for i, inquiry_data in enumerate(inquiries_data):
        inquiry_data['created_at'] = base_date - timedelta(days=i * 3, hours=i * 5)
        Inquiry.objects.create(**inquiry_data)


def remove_mock_data(apps, schema_editor):
    Property = apps.get_model('properties', 'Property')
    Inquiry = apps.get_model('properties', 'Inquiry')

    # Delete all inquiries first (due to foreign key constraint)
    Inquiry.objects.all().delete()
    # Then delete all properties
    Property.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_mock_data, remove_mock_data),
    ]
