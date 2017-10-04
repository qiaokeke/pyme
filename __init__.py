from web import accessController
import sys

sys.path.append('.')
sys.path.append('web')
sys.path.append('service')

if __name__ == '__main__':
    accessController.app.run(host='0.0.0.0')
