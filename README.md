# multi_tier_multi_threaded_tcp_servers-


#Client:
A client connects to Main Server and requests any of the three services. The client provides all necessary
details and gets desired results.

#Main Server:
This multi-threaded server has the information about where each service is implemented. Whenever a client
requests a service, the server creates a thread to serve the request. The request is then served in collaboration
with relevant Service Provider Server.
#Service Provider Servers:
These servers actually implement a service. A total of 03 such servers are to be implemented with following
details:
• Server1 is an echo service i.e., returns the same string back as passed to it.
• Server2 is a palindrome service i.e., it return whether given string is palindrome or not.
• Server3 simply returns length of a given string.
