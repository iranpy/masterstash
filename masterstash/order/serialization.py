from marshmallow import Schema, fields

class FinalizedOrderSchema(Schema):
    OrderId = fields.Str(attribute='OrderId', required=True, dump_only=True)
    PaymentTransactionId = fields.Str(attribute='PaymentTransactionId', required=True, dump_only=True)