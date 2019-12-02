# Check DNS
See if the names resolve with the provided dns servers. 

### Dev Pre-Reqs
- Docker
- Python 3.6+
- python virtualenv

### Setup and Usage
#### Local
- Create and activate a virtual environment
- Setup the environment variables or replace the values in the script.
    - ADDRESS_LIST => The list of addresses to check separated with |
    - NAME_SERVER_LIST => The list of name servers to use separated with |
- In the virtual environment:
    - run ```python -m pip install dnspython```
    - run the script with ```python ./pacth/to/main.py```
    
#### With Docker
- Run ```docker build . -t py-dns```
- run ```docker run -it py-dns python main.py```
    

