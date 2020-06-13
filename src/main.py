# main.py - Execute the unit tests on the esp board

from ujwt.jwt import Jwt

print("Unit tests")
jwt = Jwt("your-256-bit-secret")
token = jwt.encode({"name": "sbi"}).decode('utf-8')
expectedToken = "eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJIUzI1NiJ9.eyJuYW1lIjogInNiaSJ9.IcnRiWc0tEIuk6q-YmUwXUz7OmGxZ7S2f2jUWsrzuRE"
print("Test1 ==> %s" % (expectedToken == token))


token = jwt.encode({"sub": "1234567890", "name": "John Doe", "iat": 1516239022}).decode('utf-8')
expectedToken = "eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJIUzI1NiJ9.eyJzdWIiOiAiMTIzNDU2Nzg5MCIsICJuYW1lIjogIkpvaG4gRG9lIiwgImlhdCI6IDE1MTYyMzkwMjJ9.AsEihwi_vimteFklisPmU1G964FS1_-tA5GnidS6-cA"
print("Test2 ==> %s" % (expectedToken == token))

jwt2 = Jwt("367C4C4D-5563-459E-AC8A-FDAFBFF026FB")
token = jwt2.encode({"name": "tester"}).decode('utf-8')
expectedToken = "eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJIUzI1NiJ9.eyJuYW1lIjogInRlc3RlciJ9.ikY_Qy07PesT6N-x0lwegn537wA8bi2Lo5LQRdlYi7Q"
print("Test3 ==> %s" % (expectedToken == token))
