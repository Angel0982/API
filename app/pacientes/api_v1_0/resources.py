from flask import request, Blueprint
from flask_restful import Api, Resource

# Importar los modelos Paciente, Doctor, Enfermero, Camillero y Usuario
#from .models import Paciente, Doctor, Enfermero, Camillero, Usuario
#from .schemas import HumedadSchema, TemperaturaSchema
#from ..models import Humedad, Temperatura, Usuario

from .schemas import PacienteSchema
from ..models import Paciente

pacientes_v1_0_bp = Blueprint('pacientes_v1_0_bp', __name__)
api = Api(pacientes_v1_0_bp)

#humedad_schema = HumedadSchema()
#temperatura_schema = TemperaturaSchema()

paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)
class PacienteListResource(Resource):
    def get(self):
        pacientes = Paciente.query.all()
        result = pacientes_schema.dump(pacientes)
        return result

    def post(self):
        data = request.get_json()
        paciente_dict = paciente_schema.load(data)
        paciente = Paciente(**paciente_dict)
        paciente.save()
        resp = paciente_schema.dump(paciente)
        return resp, 201

class PacienteResource(Resource):
    def get(self, paciente_id):
        paciente = Paciente.query.get(paciente_id)
        if paciente is None:
            raise ObjectNotFound('El paciente no existe')
        resp = paciente_schema.dump(paciente)
        return resp

    def put(self, paciente_id):
        paciente = Paciente.query.get(paciente_id)
        data = request.get_json()
        paciente_dict = paciente_schema.load(data)
        for key, value in paciente_dict.items():
            setattr(paciente, key, value)
        paciente.save()
        resp = paciente_schema.dump(paciente)
        return resp, 200

    #def delete(self, humedad_id):
    #    humedad = Humedad.get_by_id(humedad_id)
    #    humedad.delete()
    #    return "", 204
    
    # Borrado Lógico
    def delete(self, paciente_id):
        paciente = Paciente.get_by_id (paciente_id)
        paciente.estado = 'Inactivo'
        paciente.save()
        resp = paciente_schema.dump(paciente)
        return resp, 200

class TemperaturaListResource(Resource):
    def get(self):
        pass
    
    def post(self):
        pass

class TemperaturaResource(Resource):
    def get(self, temperatura_id):
        pass
    
    def put(self, temperatura_id):
        pass

    def delete(self, temperatura_id):
        pass

#api.add_resource(HumedadListResource, '/api/v1.0/humedad/', endpoint='humedad_list_resource')
#api.add_resource(HumedadResource, '/api/v1.0/humedad/<int:humedad_id>', endpoint='humedad_resource')
#api.add_resource(TemperaturaListResource, '/api/v1.0/temperatura/', endpoint='temperatura_list_resource')
#api.add_resource(TemperaturaResource, '/api/v1.0/temperatura/<int:temperatura_id>', endpoint='temperatura_resource')
api.add_resource(PacienteListResource, '/api/v1.0/pacientes/', endpoint='paciente_list_resource')
api.add_resource(PacienteResource, '/api/v1.0/pacientes/<int:paciente_id>', endpoint='paciente_resource')