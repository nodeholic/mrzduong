from flask import Flask, request, jsonify
from mrz.generator.td1 import TD1CodeGenerator
from mrz.generator.td2 import TD2CodeGenerator
from mrz.generator.td3 import TD3CodeGenerator
from mrz.generator.mrva import MRVACodeGenerator
from mrz.generator.mrvb import MRVBCodeGenerator

app = Flask(__name__)

@app.route('/generate_mrz', methods=['GET'])
def generate_mrz():
    doc_type = request.args.get('doc_type', 'P')
    country_code = request.args.get('country_code', 'GBR')
    surname = request.args.get('surname', 'SXNGND')
    given_names = request.args.get('given_names', 'MGGPJ')
    document_number = request.args.get('document_number', 'K1RELFC7')
    birth_date = request.args.get('birth_date', '210118')
    sex = request.args.get('sex', 'F')
    expiry_date = request.args.get('expiry_date', '240710')
    optional_data1 = request.args.get('optional_data1', '')
    optional_data2 = request.args.get('optional_data2', '')

    try:
        if doc_type == 'TD1':
            result = str(TD1CodeGenerator('I', country_code, document_number, birth_date, sex, expiry_date, country_code, surname, given_names, optional_data1, optional_data2))
        elif doc_type == 'TD2':
            result = str(TD2CodeGenerator('I', country_code, surname, given_names, document_number, country_code, birth_date, sex, expiry_date, optional_data1))
        elif doc_type == 'TD3':
            result = str(TD3CodeGenerator('P', country_code, surname, given_names, document_number, country_code, birth_date, sex, expiry_date, optional_data1))
        elif doc_type == 'MRVA':
            result = str(MRVACodeGenerator('V', country_code, surname, given_names, document_number, country_code, birth_date, sex, expiry_date, optional_data1))
        elif doc_type == 'MRVB':
            result = str(MRVBCodeGenerator('V', country_code, surname, given_names, document_number, country_code, birth_date, sex, expiry_date, optional_data1))
        else:
            result = 'Invalid document type'

        return jsonify({'mrz': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
