from flask import Flask
from flask_cors import CORS
import mocks.mocks_manager as mock

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/purchase-orders/', methods=['GET'])
def get_orders():
    return mock.read_mock_json(mock.MOCK_ID_GET_ALL)


@app.route('/api/v1/purchase-orders/<order_id>', methods=['GET'])
def get_order_by_id(order_id):
    print(f"Requested ID: {order_id}")
    return mock.read_mock_json(mock.MOCK_ID_GET_ONE)


@app.route('/api/v1/purchase-orders/', methods=['POST'])
def create_order():
    return mock.read_mock_json(mock.MOCK_ID_POST)


@app.route('/api/v1/purchase-orders/<order_id>', methods=['PUT'])
def modify_order_by_id(order_id):
    print(f"Requested ID: {order_id}")
    return mock.read_mock_json(mock.MOCK_ID_PUT)


if __name__ == '__main__':
    app.run()
