class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ("com", "bg", "org", "net")

email = input()

while email != "End":
    if "@" in email:
        name, domain = email.split("@")
    else:
        raise MustContainAtSymbolError("Email must contain @")

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    else:
        domain_name, top_lvl_domain = domain.split(".")
    if top_lvl_domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
