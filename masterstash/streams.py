# from marshmallow import Schema, fields


# class BaseStream(object):
#     def __init__(self, fn, loop,  *args, **kwargs):
#         self.loop = loop
#         self.fn = fn
#         self.current = 0

#     def __call__(self, *args, **kwargs):
#         return self.fn(self.loop)
        
#     # def __iter__(self):
#     #     return self

#     # def __next__(self):
#     #     if self.current > 3:
#     #         raise StopIteration
#     #     self.current += 1
#     #     return self.current

#     def enumerate(self):
#         pass
#     def take(self):
#         pass

# class Agent(object):
#     def __init__(self, *args, **kwargs):
#         pass

#     def __call__(self, *args, **kwargs):
#         pass

# class BaseApp(object):

#     def __init__(self, *args, **kwargs):
#         self.loop = None
#         self.x = [20, 1, 2, 35] #iterator type
    
#     def iter_fn(self):
#         raise NotImplementedError

#     def _set_loop(self, loop):
#         self.loop = loop

#     def agent(self, name=None, value_type=None, **kwargs):
#         def _inner(fn):
#             loop = self.iter_fn()
#             stream = BaseStream(fn, loop)
#             return stream
#         return _inner
    
#     def task(self):
#         pass

#     def timer(self):
#         pass

#     def _on_agent_error(self):
#         print('error ...!!!')

# class RabbitStremMixin(BaseApp):
#     def __init__(self, *args, **kwargs):
#         self.loop = None
#         self.x = [20, 1, 2, 35] # sample iterator type
    
#     def iter_fn(self):
#         for i in self.x:
#             yield i

# class RabbitClient(RabbitStremMixin):
#     pass

# rb = RabbitClient()

# class ValueSchema(Schema):
#     id = fields.Str()
#     title = fields.Str()

# @rb.agent(value_type=ValueSchema)
# def sl(x):
#     for i in x:
#         pass


from kombu import Connection, Exchange, Queue

media_exchange = Exchange('first_exchange', 'topic', durable=False)

with Connection('amqp://admin:admin@localhost:5672//') as conn:
    producer = conn.Producer(serializer='json')
    producer.publish({'OrderId': 'sample1'},
                      exchange=media_exchange, routing_key='first_routing_key')
