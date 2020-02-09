from django.shortcuts import render
from .models import ResultPoolService, PoolCompare
from _sha3 import sha3_512

# Create your views here.
# def put_with_ticket(ticket, text, pool):
#     a = ResultPoolService(ticket=ticket, text=text, pool=pool)
#     a.save()
    
def put(text, pool, ticket=''):
    if ticket == '':
        ticket = sha3_512((text + str(pool)).encode('utf-8')).hexdigest()
    a = ResultPoolService(ticket=ticket, text=text, pool=pool)
    a.save()

def subscribe(pool1, pool2):
    if PoolCompare.objects.filter(result_pool=pool1, service_pool=pool2).count() < 1:
        a = PoolCompare(result_pool=pool1, service_pool=pool2)
        a.save()
    else:
        return 'error'
    
def unsubscribe(pool1, pool2):
    PoolCompare.objects.filter(result_pool=pool1, service_pool=pool2).delete()
    
def get(pool, ticket=''):
    try:
        if ticket == '':
            a = ResultPoolService.objects.filter(pool=pool).first()
            ResultPoolService.objects.filter(pool=pool).first().delete()
        else:
            a = ResultPoolService.objects.get(ticket=ticket)
            ResultPoolService.objects.get(ticket=ticket).delete()
        return a
    except:
        return None
        
    
    
        
    
    