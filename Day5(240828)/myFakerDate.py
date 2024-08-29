from faker import Faker

fake = Faker("ko-KR")
name = fake.name()
print(name)

test_data = [(fake.name(), fake.address()) for i in range(30)]
print(test_data)
