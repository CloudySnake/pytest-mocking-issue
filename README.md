# pytest-mocking-issue
I have had an issue with mocked objects leaking across tests causing failures in 
otherwise acceptable tests (when run separately everything works fine).  

https://stackoverflow.com/questions/7293653/mocking-before-importing-a-module

That link largely solved my problem. As I'm creating a connection _outside_ of my handler
(to for more efficient use of the connection) I need to mock both the source connection
code (to stop it trying to instantiate and connect) and also then the specific instance of
my connection the handler is using.

I've also played with module and session scoping as that looks useful for other things I'm looking at.