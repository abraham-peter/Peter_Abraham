def cautare_hash_table_pe_mod1000(hash_test,cnpuri_cautate_test):
        counter_iteratii_lista=[]
        for cnp_random in _test:
            iteratii=0
            for keys,values in cnpuri_cautate_test.items():
                iteratii+=1
                if cnp_random==values:
                    counter_iteratii_lista.append(iteratii)
        if counter_iteratii_lista:
            min_iterations = min(counter_iteratii_lista)
            max_iterations = max(counter_iteratii_lista)
            print("Statistici de cautare")
            print(f"Minimum iterations: {min_iterations}")
            print(f"Maximum iterations: {max_iterations}")