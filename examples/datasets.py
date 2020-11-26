import asencis

if __name__ == "__main__":
    response = asencis.Datasets.list()
    # print(response.json())
    print(response)

    response = asencis.Datasets.retrieve(uuid="e7133620-954e-4db4-a4a4-ac98792fee9e")
    print(response.json())
    print(response)
