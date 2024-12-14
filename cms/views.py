from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Схемы для отдельных элементов
title_schema = openapi.Schema(type=openapi.TYPE_OBJECT,
    properties={'title': openapi.Schema(type=openapi.TYPE_STRING)})

subtitle_schema = openapi.Schema(type=openapi.TYPE_OBJECT,
    properties={'subtitle': openapi.Schema(type=openapi.TYPE_STRING)})

button_schema = openapi.Schema(type=openapi.TYPE_OBJECT,
    properties={
        'button_text': openapi.Schema(type=openapi.TYPE_STRING),
        'button_link': openapi.Schema(type=openapi.TYPE_STRING)
    })

image_schema = openapi.Schema(type=openapi.TYPE_OBJECT,
    properties={'illustration_path': openapi.Schema(type=openapi.TYPE_STRING)})

full_schema = openapi.Schema(type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING),
        'subtitle': openapi.Schema(type=openapi.TYPE_STRING),
        'button_text': openapi.Schema(type=openapi.TYPE_STRING),
        'button_link': openapi.Schema(type=openapi.TYPE_STRING),
        'illustration_path': openapi.Schema(type=openapi.TYPE_STRING),
    })

# First Page
@swagger_auto_schema(method='get', responses={200: full_schema})
@swagger_auto_schema(method='put', request_body=full_schema, responses={200: full_schema})
@swagger_auto_schema(method='patch', request_body=full_schema, responses={200: full_schema})
@api_view(['GET', 'PUT', 'PATCH'])
def first_page(request):
    """First Page - полное управление контентом"""
    if request.method == 'GET':
        return Response({
            'title': 'The first choice of the successful!',
            'subtitle': 'Take the first step to success with the market leaders!',
            'button_text': 'See all service',
            'button_link': '/service',
            'illustration_path': '/assets/main.svg'
        })
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: title_schema})
@swagger_auto_schema(method='put', request_body=title_schema, responses={200: title_schema})
@api_view(['GET', 'PUT'])
def first_page_title(request):
    """First Page - управление заголовком"""
    if request.method == 'GET':
        return Response({'title': 'The first choice of the successful!'})
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: subtitle_schema})
@swagger_auto_schema(method='put', request_body=subtitle_schema, responses={200: subtitle_schema})
@api_view(['GET', 'PUT'])
def first_page_subtitle(request):
    """First Page - управление подзаголовком"""
    if request.method == 'GET':
        return Response({'subtitle': 'Take the first step to success with the market leaders!'})
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: button_schema})
@swagger_auto_schema(method='put', request_body=button_schema, responses={200: button_schema})
@api_view(['GET', 'PUT'])
def first_page_button(request):
    """First Page - управление кнопкой"""
    if request.method == 'GET':
        return Response({
            'button_text': 'See all service',
            'button_link': '/service'
        })
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: image_schema})
@swagger_auto_schema(method='put', request_body=image_schema, responses={200: image_schema})
@api_view(['GET', 'PUT'])
def first_page_image(request):
    """First Page - управление изображением"""
    if request.method == 'GET':
        return Response({'illustration_path': '/assets/main.svg'})
    return Response(request.data)

# Second Page
@swagger_auto_schema(method='get', responses={200: full_schema})
@swagger_auto_schema(method='put', request_body=full_schema, responses={200: full_schema})
@swagger_auto_schema(method='patch', request_body=full_schema, responses={200: full_schema})
@api_view(['GET', 'PUT', 'PATCH'])
def second_page(request):
    """Second Page - полное управление контентом"""
    if request.method == 'GET':
        return Response({
            'title': '1C: Solutions that work for you!',
            'subtitle': 'We offer software that works for you, helping you achieve your goal.',
            'button_text': 'See all service',
            'button_link': '/service',
            'illustration_path': '/assets/inllustration.svg'
        })
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: title_schema})
@swagger_auto_schema(method='put', request_body=title_schema, responses={200: title_schema})
@api_view(['GET', 'PUT'])
def second_page_title(request):
    """Second Page - управление заголовком"""
    if request.method == 'GET':
        return Response({'title': '1C: Solutions that work for you!'})
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: subtitle_schema})
@swagger_auto_schema(method='put', request_body=subtitle_schema, responses={200: subtitle_schema})
@api_view(['GET', 'PUT'])
def second_page_subtitle(request):
    """Second Page - управление подзаголовком"""
    if request.method == 'GET':
        return Response({'subtitle': 'We offer software that works for you, helping you achieve your goal.'})
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: button_schema})
@swagger_auto_schema(method='put', request_body=button_schema, responses={200: button_schema})
@api_view(['GET', 'PUT'])
def second_page_button(request):
    """Second Page - управление кнопкой"""
    if request.method == 'GET':
        return Response({
            'button_text': 'See all service',
            'button_link': '/service'
        })
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: image_schema})
@swagger_auto_schema(method='put', request_body=image_schema, responses={200: image_schema})
@api_view(['GET', 'PUT'])
def second_page_image(request):
    """Second Page - управление изображением"""
    if request.method == 'GET':
        return Response({'illustration_path': '/assets/inllustration.svg'})
    return Response(request.data)

# Third Page
@swagger_auto_schema(method='get', responses={200: full_schema})
@swagger_auto_schema(method='put', request_body=full_schema, responses={200: full_schema})
@swagger_auto_schema(method='patch', request_body=full_schema, responses={200: full_schema})
@api_view(['GET', 'PUT', 'PATCH'])
def third_page(request):
    """Third Page - полное управление контентом"""
    if request.method == 'GET':
        return Response({
            'title': 'Quick start for your business with 1C',
            'subtitle': 'Our 1C software will help you get started quickly and hassle-free.',
            'button_text': 'See all service',
            'button_link': '/service',
            'illustration_path': '/assets/illustration2.svg'
        })
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: title_schema})
@swagger_auto_schema(method='put', request_body=title_schema, responses={200: title_schema})
@api_view(['GET', 'PUT'])
def third_page_title(request):
    """Third Page - управление заголовком"""
    if request.method == 'GET':
        return Response({'title': 'Quick start for your business with 1C'})
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: subtitle_schema})
@swagger_auto_schema(method='put', request_body=subtitle_schema, responses={200: subtitle_schema})
@api_view(['GET', 'PUT'])
def third_page_subtitle(request):
    """Third Page - управление подзаголовком"""
    if request.method == 'GET':
        return Response({'subtitle': 'Our 1C software will help you get started quickly and hassle-free.'})
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: button_schema})
@swagger_auto_schema(method='put', request_body=button_schema, responses={200: button_schema})
@api_view(['GET', 'PUT'])
def third_page_button(request):
    """Third Page - управление кнопкой"""
    if request.method == 'GET':
        return Response({
            'button_text': 'See all service',
            'button_link': '/service'
        })
    return Response(request.data)

@swagger_auto_schema(method='get', responses={200: image_schema})
@swagger_auto_schema(method='put', request_body=image_schema, responses={200: image_schema})
@api_view(['GET', 'PUT'])
def third_page_image(request):
    """Third Page - управление изображением"""
    if request.method == 'GET':
        return Response({'illustration_path': '/assets/illustration2.svg'})
    return Response(request.data)