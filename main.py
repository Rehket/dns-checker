import dns.resolver
import logging
import os
import sys
logging.basicConfig(level=logging.INFO)

address_list = os.getenv("ADDRESS_LIST", None)
# address_list = os.getenv("ADDRESS_LIST", "google.com|officedepot.com|bad_broken.add.ress")

name_server_list = os.getenv("NAME_SERVER_LIST", None)
# name_server_list = os.getenv("NAME_SERVER_LIST", "1.1.1.1|8.8.8.8|8.8.4.4")

if __name__ == "__main__":

    if name_server_list is None:
        logging.error("No name servers provided!"
                      "Set the NAME_SERVER_LIST environment variable to a bar(|) delimited string of name servers!")
        sys.exit(-1)
    name_server_list = name_server_list.split("|")
    logging.info(f"Name Servers: {name_server_list}")

    if address_list is None:
        logging.error("No address list provided!"
                      "Set the ADDRESS_LIST environment variable to a bar(|) delimited string of addresses!")
        sys.exit(-1)
    address_list = address_list.split("|")
    logging.info(f"Address List: {address_list}")

    my_resolver = dns.resolver.Resolver(configure=False)
    my_resolver.nameservers = ["1.1.1.1", "8.8.8.8"]

    for address in address_list:
        try:
            result = my_resolver.query(address)
            logging.info(f"Response for {address} canonical_name: {result.canonical_name}")
        except dns.resolver.NXDOMAIN as e:
            logging.error(f"{address} could not be resolved! Sound the alarm!")
        except Exception as e:
            logging.error(f"Something unexpected broke! Sound the alarm!")
            logging.error(e)


