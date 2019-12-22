import sys
print(sys.path)
from src.service import admin_service


if __name__ == '__main__':
    admin_service.main()