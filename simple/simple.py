# Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
# edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
# elementos. retornar la lista.
import random;

list = [];
def generate():
    for i in range(10):
        list.append({"id":i, "edad":random.randint(1,100)})
        print(list[i]);
    return list;

# Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
# menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.

def order(list):
    list.sort(key=lambda x: x["edad"], reverse=True)
    print("La persona más vieja es: ", list[0]["id"]);
    print("La persona más joven es: ", list[-1]["id"]);
    print(list);
    return list;


generate();
order(list);
