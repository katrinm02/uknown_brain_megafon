from .models import PoolServices, PoolPending
import datetime
from _sha3 import sha3_512


def getNow():
    return datetime.datetime.now()
 

def register(endpoint, pool):
    if PoolServices.objects.filter(endpoint=endpoint):
        if PoolServices.objects.filter(endpoint=endpoint, pool=pool):
            ticket = PoolServices.objects.filter(endpoint=endpoint, pool=pool)[0]
        else:
            return 'error'    
    else:
        ticket = sha3_512((endpoint + str(pool)).encode('utf-8')).hexdigest()
        q = PoolServices(ticket=ticket, endpoint=endpoint, pool=pool, timestamp=getNow())
        q.save()
        return ticket
    
    
def unregister(ticket):
    PoolServices.objects.filter(ticket=ticket).delete()

    
def update(ticket, state):
    checkPending()
    PoolServices.objects.filter(ticket=ticket).update(state=state, timestamp=getNow())

    
def getWork(pool):
    checkOld()
    checkPending()
    if PoolServices.objects.filter(pool=pool, state='SA').count() < 1:
        return None
    else:
        PoolServices.objects.filter(pool=pool).update(state = 'SP', timestamp=getNow())
        for obj in PoolServices.objects.filter(pool=pool).all():
            a = PoolPending(ticket=obj, timer=getNow())
            a.save()
            return obj.endpoint
        
          
def checkPending():
    for i in PoolPending.objects.all():
        then = i.timer
        if (getNow() - then).seconds > 40:
            PoolServices.objects.filter(ticket=i.ticket.ticket).update(state='SA', timestamp=getNow())
            i.delete()
            
               
def checkOld():
    for i in PoolServices.objects.all():
        then = i.timestamp
        if (getNow() - then).seconds > 60:
            i.delete()
    
            
            
        
        
        
        
        