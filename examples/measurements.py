import asencis

if __name__ == "__main__":
    response = asencis.Prefixes.list()
    # print(response.json())
    print(response)

    response = asencis.Quantities.list()
    # print(response.json())
    print(response)
