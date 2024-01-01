import json
import graphene

class ResponseObject(graphene.ObjectType):
    id = graphene.String()
    status = graphene.Boolean()
    code = graphene.Int()
    message = graphene.String()

    def __read_code_file(code_id):
        file = open('response_codes.json', 'r')
        file_codes = file.read()
        response_codes = json.loads(file_codes)
        response_code = next(code for code in response_codes if code["id"] == code_id)
        print(response_code)
        return response_code

    def get_response(id):
        try:

            response_code = ResponseObject.__read_code_file(id)
            
            return ResponseObject(
                response_code['id'],
                response_code['status'],
                response_code['code'],
                response_code['message'],
            )
        except Exception as e:
            print(e)
            return ResponseObject()
        


