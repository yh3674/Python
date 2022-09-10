dataFilePath = "Practice_Pokemon/pokemon_data.txt"

indexFilePath = "Practice_Pokemon/pokemon_index.txt"

# 1. indexfile read ==> Creating a list with names of pokemon


pokemon_name_list = list()

fstream = open(indexFilePath,encoding="utf-8") # In case of data written in Korea, must ,encoding utf-8
temp_list = fstream.readlines()

for i in temp_list:
    pokemon_name_list.append(i.strip()) # Read 후 \n을 제거하고 => 리스트에 추가

fstream.close()



# 2. 포켓몬 이름이 있는 리스트와 동일한 길이의 리스트 create, 0으로 reset

pokemon_count_list = list()

for i in pokemon_name_list : 
    pokemon_count_list.append(0)



print(len(pokemon_name_list))
print(len(pokemon_count_list))

# 3.Data file read => while 반복문으로 돌리면서 해당 포켓몬이 들어있는 값 얻기

fstream = open(dataFilePath,encoding="utf-8")
all_pokemonData_list = fstream.readlines()
for each in all_pokemonData_list :
    each_pokemon = each.strip()
    target_index = pokemon_name_list.index(each_pokemon)

# 4. 0으로 reset된 list d위에서 찾았던 index 번호에 -1

    pokemon_count_list[target_index] += 1 # pokemon_count_list[target_index] + 1

fstream.close

# Print

for i in range( len(pokemon_count_list) ) : # length of list 8
    print(pokemon_name_list[i], " : ", pokemon_count_list[i])
