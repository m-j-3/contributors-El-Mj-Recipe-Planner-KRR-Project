from recipe_scrapers import scrape_me
import PySimpleGUI as gui
import webbrowser

gui.theme("DarkBlue")

# ingredient class, keeps track of various important details
class Ingredient:
    isAList = []
    genLList = []
    allergens = []

    def __init__(self, name):
        self.name = name

    def isA(self, type):
        self.isAList.append(type)

    def genL(self, type):
        self.genLList.append(type)
        type.instance(self)

    def allergen(self, item):
        self.allergens.append(item)

    # for some reason, this is necessary on initialization
    # otherwise, these lists start out with random stuff in them
    def clean(self):
        self.isAList = []
        self.genLList = []
        self.allergens = []

# genL class, subclass of ingredients but also has a list of instances
# list of instances may not actually ever be used
# wanted to keep track of it just in case
class GenL(Ingredient):
    instances = []

    def clean(self):
        self.isAList = []
        self.genLList = []
        self.allergens = []
        self.instances = []

    def instance(self, item):
        self.instances.append(item)


ingredient_list = []
genL_list = []

# list of all of our recipes, if you want to add a new recipe, you can add it here
recipe_urls = ['https://www.allrecipes.com/recipe/235158/worlds-best-honey-garlic-pork-chops/',
               'https://www.allrecipes.com/recipe/229324/ground-beef-and-cabbage/',
               'https://www.allrecipes.com/recipe/280052/bbq-chicken-breasts-in-the-oven/',
               'https://www.allrecipes.com/recipe/245367/pan-roasted-chicken-breasts/',
               'https://www.allrecipes.com/recipe/231939/honey-glazed-chicken/',
               'https://www.allrecipes.com/recipe/8495/chicken-cordon-bleu-i/',
               'https://www.allrecipes.com/recipe/244458/buttered-noodles/']

# parse recipes from URLs
# gives methods .ingredients(), .instructions(), .instructions_list(), .title(), .total_time()
recipes = []
for i in recipe_urls:
    recipes.append([[], scrape_me(i), i])

# all genLs

milk_product = GenL('milk product')
milk_product.clean()
milk_product.allergen('lactose')
genL_list.append(milk_product)

cheese = GenL('cheese')
cheese.clean()
cheese.isA('cheese')
cheese.genL(milk_product)
genL_list.append(cheese)

animal_product = GenL('animal product')
animal_product.clean()
animal_product.allergen('vegan')
animal_product.allergen('vegetarian')
genL_list.append(animal_product)

meat_product = GenL('meat product')
meat_product.clean()
meat_product.isA('protein')
meat_product.genL(animal_product)
genL_list.append(meat_product)

peanut_product = GenL('peanut product')
peanut_product.clean()
peanut_product.allergen('peanut')
genL_list.append(peanut_product)

nonstick_element = GenL('nonstick element')
nonstick_element.clean()
nonstick_element.isA('nonstick element')
genL_list.append(nonstick_element)

spice = GenL('spice')
spice.clean()
spice.isA('spice')
spice.isA('seasoning')
genL_list.append(spice)

tree_nut = GenL('tree nut')
tree_nut.clean()
tree_nut.isA('tree nut')
tree_nut.allergen('tree nut')
genL_list.append(tree_nut)

coating = GenL('coating')
coating.clean()
coating.isA('coating')
genL_list.append(coating)

noodle = GenL('noodle')
noodle.clean()
noodle.isA('noodle')
genL_list.append(noodle)

# all ingredients

ketchup = Ingredient('ketchup')
ketchup.clean()
ketchup.isA('condiment')
ingredient_list.append(ketchup)

honey = Ingredient('honey')
honey.clean()
honey.isA('sauce')
ingredient_list.append(honey)

soy_sauce = Ingredient('soy sauce')
soy_sauce.clean()
soy_sauce.isA('sauce')
ingredient_list.append(soy_sauce)

garlic = Ingredient('garlic')
garlic.clean()
garlic.genL(spice)
ingredient_list.append(garlic)

pork_chop = Ingredient('pork chop')
pork_chop.clean()
pork_chop.genL(meat_product)
ingredient_list.append(pork_chop)

cabbage = Ingredient('cabbage')
cabbage.clean()
cabbage.isA('leafy green')
ingredient_list.append(cabbage)

tomato = Ingredient('tomato')
tomato.clean()
tomato.isA('vegetable')
ingredient_list.append(tomato)

onion = Ingredient('onion')
onion.clean()
onion.isA('alliaceae')
ingredient_list.append(onion)

italian_seasoning = Ingredient('italian seasoning')
italian_seasoning.clean()
italian_seasoning.genL(spice)
ingredient_list.append(italian_seasoning)

salt_and_pepper = Ingredient('salt and ground black pepper')
salt_and_pepper.clean()
salt_and_pepper.genL(spice)
ingredient_list.append(salt_and_pepper)

ground_beef = Ingredient('ground beef')
ground_beef.clean()
ground_beef.genL(meat_product)
ingredient_list.append(ground_beef)

chicken_breast = Ingredient('chicken breast')
chicken_breast.clean()
chicken_breast.genL(meat_product)
ingredient_list.append(chicken_breast)

barbecue_sauce = Ingredient('barbecue sauce')
barbecue_sauce.clean()
barbecue_sauce.isA('sauce')
ingredient_list.append(barbecue_sauce)

olive_oil = Ingredient('olive oil')
olive_oil.clean()
olive_oil.isA('cooking oil')
ingredient_list.append(olive_oil)

thyme = Ingredient('thyme')
thyme.clean()
thyme.genL(spice)
ingredient_list.append(thyme)

parsley = Ingredient('parsley')
parsley.clean()
parsley.genL(spice)
ingredient_list.append(parsley)

rosemary = Ingredient('rosemary')
rosemary.clean()
rosemary.genL(spice)
ingredient_list.append(rosemary)

apple_cider_vinegar = Ingredient('apple cider vinegar')
apple_cider_vinegar.clean()
apple_cider_vinegar.isA('vinegar')
ingredient_list.append(apple_cider_vinegar)

butter = Ingredient('butter')
butter.clean()
butter.isA('butter')
butter.genL(milk_product)
ingredient_list.append(butter)

chicken_broth = Ingredient('chicken broth')
chicken_broth.clean()
chicken_broth.isA('broth')
chicken_broth.genL(animal_product)
ingredient_list.append(chicken_broth)

red_pepper = Ingredient('red pepper flake')
red_pepper.clean()
red_pepper.genL(spice)
ingredient_list.append(red_pepper)

cooking_spray = Ingredient('cooking spray')
cooking_spray.clean()
cooking_spray.genL(nonstick_element)
ingredient_list.append(cooking_spray)

salt = Ingredient('salt')
salt.clean()
salt.genL(spice)
ingredient_list.append(salt)

black_pepper = Ingredient('black pepper')
black_pepper.clean()
black_pepper.genL(spice)
ingredient_list.append(black_pepper)

swiss_cheese = Ingredient('swiss cheese')
swiss_cheese.clean()
swiss_cheese.genL(cheese)
ingredient_list.append(swiss_cheese)

ham = Ingredient('ham')
ham.clean()
ham.genL(meat_product)
ingredient_list.append(ham)

bread_crumbs = Ingredient('bread crumbs')
bread_crumbs.clean()
bread_crumbs.genL(coating)
ingredient_list.append(bread_crumbs)

fettuccine = Ingredient('fettuccine')
fettuccine.clean()
fettuccine.genL(noodle)
ingredient_list.append(fettuccine)

# ingredients not in recipes but added as potential substitutes

american_cheese = Ingredient('american cheese')
american_cheese.clean()
american_cheese.genL(cheese)
ingredient_list.append(american_cheese)

mozzarella = Ingredient('mozzarella')
mozzarella.clean()
mozzarella.genL(cheese)
ingredient_list.append(mozzarella)

parmesan_cheese = Ingredient('parmesan cheese')
parmesan_cheese.clean()
parmesan_cheese.genL(cheese)
ingredient_list.append(parmesan_cheese)

provolone_cheese = Ingredient('provolone cheese')
provolone_cheese.clean()
provolone_cheese.genL(cheese)
ingredient_list.append(provolone_cheese)

crackers = Ingredient('crackers')
crackers.clean()
crackers.genL(coating)
ingredient_list.append(crackers)

almond = Ingredient('almond')
almond.clean()
almond.genL(coating)
almond.genL(tree_nut)
ingredient_list.append(almond)

peanut = Ingredient('peanut')
peanut.clean()
peanut.genL(coating)
peanut.genL(peanut_product)
ingredient_list.append(peanut)

coconut_oil = Ingredient('coconut oil')
coconut_oil.clean()
coconut_oil.genL(tree_nut)
coconut_oil.isA('butter')
ingredient_list.append(coconut_oil)

pam = Ingredient('pam')
pam.clean()
pam.genL(nonstick_element)
ingredient_list.append(pam)

vegetable_broth = Ingredient('vegetable broth')
vegetable_broth.clean()
vegetable_broth.isA('broth')
ingredient_list.append(vegetable_broth)

leek = Ingredient('leek')
leek.clean()
leek.isA('alliaceae')
ingredient_list.append(leek)

shallot = Ingredient('shallot')
shallot.clean()
shallot.isA('alliaceae')
ingredient_list.append(shallot)

spaghetti = Ingredient('spaghetti')
spaghetti.clean()
spaghetti.genL(noodle)
ingredient_list.append(spaghetti)

tofu = Ingredient('tofu')
tofu.clean()
tofu.isA('protein')
ingredient_list.append(tofu)

# adding ingredients to their recipes

recipes[0][0] = [ketchup, honey, soy_sauce, garlic, pork_chop]
recipes[1][0] = [cabbage, tomato, onion, italian_seasoning, salt_and_pepper, ground_beef]
recipes[2][0] = [chicken_breast, barbecue_sauce, salt_and_pepper]
recipes[3][0] = [chicken_breast, salt_and_pepper, olive_oil, thyme, parsley, rosemary, apple_cider_vinegar, butter, chicken_broth]
recipes[4][0] = [honey, soy_sauce, red_pepper, olive_oil, chicken_breast]
recipes[5][0] = [cooking_spray, chicken_breast, salt, black_pepper, swiss_cheese, ham, bread_crumbs]
recipes[6][0] = [fettuccine, butter, salt_and_pepper, parmesan_cheese]

# user adds new ingredient into database
def new_ingredient(ing_name, lst_of_genLs, lst_of_isAs, lst_of_allergens):
    new_ing = Ingredient(ing_name)
    new_ing.clean()
    for i in lst_of_genLs:
        if i != '':
            new_ing.genL(i)
    for j in lst_of_isAs:
        if j != '':
            new_ing.isA(j)
    for k in lst_of_allergens:
        if k != '':
            new_ing.allergen(k)
    update_allergens(new_ing)
    update_isAs(new_ing)
    ingredient_list.append(new_ing)

# user adds new genL into database
def new_genL(genL_name, lst_of_genLs, lst_of_isAs, lst_of_allergens, lst_of_instances):
    new_gL = GenL(genL_name)
    new_gL.clean()
    for i in lst_of_genLs:
        if i != '':
            new_gL.genL(i)
    for j in lst_of_isAs:
        if j != '':
            new_gL.isA(j)
    for k in lst_of_allergens:
        if k != '':
            new_gL.allergen(k)
    for l in lst_of_instances:
        if l != '':
            l.genL(new_gL)
    update_allergens(new_gL)
    update_isAs(new_gL)
    genL_list.append(new_gL)

# apply forward chaining to determine if an item has an allergy
# first build list of genLs
# then check allergens in all genLs
def update_allergens_helper(ing):
    result = [ing]
    for i in ing.genLList:
        result += update_allergens_helper(i)
    return result

def update_allergens(ing):
    genLs = update_allergens_helper(ing)
    for i in genLs:
        for j in i.allergens:
            if j not in ing.allergens:
                ing.allergen(j)
    return ing.allergens

# apply forward chaining to determine if an item is something
def update_isAs(ing):
    isAs = update_isAs_helper(ing)
    for i in isAs:
        if i not in ing.isAList:
            ing.isA(i)
    return ing.isAList

def update_isAs_helper(ing):
    result = ing.isAList
    for i in ing.genLList:
        result += update_isAs_helper(i)
    return result

# display ingredient info in a new window
def show_ing(ing_name):
    ing = False
    for i in ingredient_list: # find the ingredient object from the name
        if i.name == ing_name:
            ing = i
            break
    if ing: # if we found the ingredient, show its info
        update_isAs(ing)
        update_allergens(ing)
        ing_genLs = [] # get list of names of genLs of the ingredient
        for i in ing.genLList: 
            ing_genLs.append(i.name)
        genLs_str = '' # change list to a string
        if len(ing_genLs) > 0:
            ind = -1
            for i in ing_genLs:
                ind += 1
                if ind > 0:
                    genLs_str += ', ' + i
                else:
                    genLs_str += i
        ing_isAs = [] # do same thing for the isAs
        for i in ing.isAList: 
            ing_isAs.append(i)
        isAs_str = ''
        if len(ing_isAs) > 0:
            ind = -1
            for i in ing_isAs:
                ind += 1
                if ind > 0:
                    isAs_str += ', ' + i
                else:
                    isAs_str += i
        ing_allergens = [] # and finally for allergens
        for i in ing.allergens:
            ing_allergens.append(i)
        allergens_str = ''
        if len(ing_allergens) > 0:
            ind = -1
            for i in ing_allergens:
                ind += 1
                if ind > 0:
                    allergens_str += ', ' + i
                else:
                    allergens_str += i
        layout = [
            [gui.Text(ing_name,font=(16))],
            [gui.Text('isAs:'),
             gui.Text(isAs_str)],
            [gui.Text('genLs:'),
             gui.Text(genLs_str)],
            [gui.Text('allergens:'),
             gui.Text(allergens_str)],
            [gui.Button('Close',key='-CLOSE-')]
        ]
        window = gui.Window(ing_name + ' info',layout,size=(400,300),element_justification='center',margins=(6,20))
        while True:
            event, values = window.read()
            if event == gui.WIN_CLOSED or event == '-CLOSE-': # when window closes
                break
        window.close()

# display genL info in a new window
def show_genL(genL_name):
    genL = False
    for i in genL_list: # find the genL object from the name
        if i.name == genL_name:
            genL = i
            break
    if genL: # if we found the genL, show its info
        update_isAs(genL)
        update_allergens(genL)
        genL_genLs = [] # get list of names of genLs of the genL
        for i in genL.genLList: 
            genL_genLs.append(i.name)
        genLs_str = '' # change list to a string
        if len(genL_genLs) > 0:
            ind = -1
            for i in genL_genLs:
                ind += 1
                if ind > 0:
                    genLs_str += ', ' + i
                else:
                    genLs_str += i
        genL_isAs = [] # do same thing for the isAs
        for i in genL.isAList: 
            genL_isAs.append(i)
        isAs_str = ''
        if len(genL_isAs) > 0:
            ind = -1
            for i in genL_isAs:
                ind += 1
                if ind > 0:
                    isAs_str += ', ' + i
                else:
                    isAs_str += i
        genL_allergens = [] # and for allergens
        for i in genL.allergens:
            genL_allergens.append(i)
        allergens_str = ''
        if len(genL_allergens) > 0:
            ind = -1
            for i in genL_allergens:
                ind += 1
                if ind > 0:
                    allergens_str += ', ' + i
                else:
                    allergens_str += i
        genL_instances = [] # and finally for instances
        for i in genL.instances:
            genL_instances.append(i)
        instances_str = ''
        if len(genL_instances) > 0:
            ind = -1
            for i in genL_instances:
                ind += 1
                if ind > 0:
                    instances_str += ', ' + i.name
                else:
                    instances_str += i.name
        layout = [
            [gui.Text(genL_name,font=(16))],
            [gui.Text('isAs:'),
             gui.Text(isAs_str)],
            [gui.Text('genLs:'),
             gui.Text(genLs_str)],
            [gui.Text('allergens:'),
             gui.Text(allergens_str)],
            [gui.Text('instances:'),
             gui.Text(instances_str)],
            [gui.Button('Close',key='-CLOSE-')]
        ]
        window = gui.Window(genL_name + ' info',layout,size=(400,300),element_justification='center',margins=(6,20))
        while True:
            event, values = window.read()
            if event == gui.WIN_CLOSED or event == '-CLOSE-': # when window closes
                break
        window.close()

# makes a window so the user can add a new ingredient
def add_ingredient():
    genL_names = []
    for i in genL_list:
        genL_names.append(i.name)
    layout = [
        [gui.Text('Add an ingredient to the database')],
        [gui.Text('Name', size =(15, 1)), gui.InputText()],
        [gui.Text('isAs: ', size =(15, 1)), gui.InputText(), gui.Text('(separate values with commas, no spaces)')],
        [gui.Text('GenLs: ', size =(15, 1)), gui.Listbox(values=genL_names,select_mode=gui.LISTBOX_SELECT_MODE_MULTIPLE),
         gui.Text('(click to highlight each of your selections)')],
        [gui.Text('Allergens: ', size =(15, 1)), gui.InputText(), gui.Text('(separate values with commas, no spaces)')],
        [gui.Submit()]
    ]
    window = gui.Window('Add an ingredient', layout, modal=True)
    event, values = window.read()
    window.close()
    if values[1] != None:
        new_name = values[0]
        new_isAs = values[1].split(',')
        new_genLs_names = values[2]
        new_genLs = []
        for i in new_genLs_names:
            for j in genL_list:
                if j.name == i:
                    new_genLs.append(j)
                    break
        new_allergens = values[3].split(',')
        new_ingredient(new_name, new_genLs, new_isAs, new_allergens)
        return True
    return False

# makes a window so the user can add a new genL
def add_genL():
    genL_names = []
    for i in genL_list:
        genL_names.append(i.name)
    ing_names = []
    for i in ingredient_list:
        ing_names.append(i.name)
    layout = [
        [gui.Text('Add a type of ingredient to the database')],
        [gui.Text('Name', size =(15, 1)), gui.InputText()],
        [gui.Text('isAs: ', size =(15, 1)), gui.InputText(), gui.Text('(separate values with commas, no spaces)')],
        [gui.Text('GenLs: ', size =(15, 1)), gui.Listbox(values=genL_names,select_mode=gui.LISTBOX_SELECT_MODE_MULTIPLE),
         gui.Text('(click to highlight each of your selections)')],
        [gui.Text('Allergens: ', size =(15, 1)), gui.InputText(), gui.Text('(separate values with commas, no spaces)')],
        [gui.Text('Instances: ', size =(15, 1)), gui.Listbox(values=ing_names,select_mode=gui.LISTBOX_SELECT_MODE_MULTIPLE),
         gui.Text('(click to highlight each of your selections)')],
        [gui.Submit()]
    ]
    window = gui.Window('Add a type of ingredient', layout, modal=True)
    event, values = window.read()
    window.close()
    if values[1] != None:
        new_name = values[0]
        new_isAs = values[1].split(',')
        new_genLs_names = values[2]
        new_genLs = []
        for i in new_genLs_names:
            for j in genL_list:
                if j.name == i:
                    new_genLs.append(j)
                    break
        new_allergens = values[3].split(',')
        new_instances_names = values[4]
        new_instances = []
        for i in new_instances_names:
            for j in ingredient_list:
                if j.name == i:
                    new_instances.append(j)
                    break
        new_genL(new_name, new_genLs, new_isAs, new_allergens, new_instances)
        return True
    return False

# window for making substitutions
def substitute(rec):
    ingredients = []
    for i in rec[0]:
        ingredients.append(i.name)
    genL_names = []
    for i in genL_list:
        genL_names.append(i.name)
    layout = [
        [gui.Text('Choose an ingredient to replace: ')], 
        [gui.Radio(text, 1) for text in ingredients],
        [gui.Text('Type any allergies, separated by commas without spaces: '),
         gui.InputText()],
        [gui.Text('Select any genLs you wish to exclude in the substitutes: '),
         gui.Listbox(values=genL_names,select_mode=gui.LISTBOX_SELECT_MODE_MULTIPLE),
         gui.Text('(click to highlight each of your selections)')],
        [gui.Button('Submit',key='-SUBMIT-')],
        [gui.Text('',key='-RESULT-')]
    ]
    window = gui.Window('Substitution', layout, modal=True)
    while True:
        event, values = window.read()
        if event == '-SUBMIT-':
            val_list = []
            for i in values:
                val_list.append(values[i])
            old_ing = get_ingredient_to_replace(val_list,rec)
            user_allergens = []
            if val_list[-2] != '':
                user_allergens = val_list[-2].split(',')
            banned_genL_names = val_list[-1]
            banned_genLs = []
            for i in banned_genL_names:
                for j in genL_list:
                    if j.name == i:
                        banned_genLs.append(j)
                        break
            if old_ing:
                possible_replacers = matcher(old_ing,user_allergens,banned_genLs)
                if len(possible_replacers) > 0:
                    replacers_str = ''
                    ind = -1
                    for i in possible_replacers:
                        ind += 1
                        if ind > 0:
                            replacers_str += ', ' + i.name
                        else:
                            replacers_str += i.name
                    window['-RESULT-'].update('Possible replacements: ' + replacers_str)
                else:
                    window['-RESULT-'].update('There are no replacements that fit the parameters.')
        elif event == gui.WIN_CLOSED:
            break
    window.close()

# helper for substitute    
def get_ingredient_to_replace(val,rec):
    ind = -1
    for i in val:
        ind += 1
        if i and not isinstance(val[i], str):
            return rec[0][ind]
    return False

# helper for matcher
def no_allergens(list1, list2):
    for val in list1:
        if val in list2:
            return False
    return True

# helper for matcher
def all_isAs(list1, list2):
    for val in list1:
        if val not in list2:
            return False
    return True

def no_genLs_helper(ele):
    result = [ele]
    for i in ele.genLList:
        result += no_genLs_helper(i)
    return result

def no_genLs(list1,list2):
    all_genLs = []
    for i in list1:
        all_genLs.append(no_genLs_helper(i))
    all_genLs_flat = [item for sublist in all_genLs for item in sublist]
    for val in all_genLs_flat:
        if val in list2:
            return False
    return True


def matcher(ing,user_allergens,banned_genLs):
    matches = []
    update_isAs(ing)
    for i in ingredient_list:
        if i != ing:
            update_allergens(i)
            update_isAs(i)
            if no_allergens(user_allergens,i.allergens) and all_isAs(ing.isAList,i.isAList) and no_genLs(i.genLList,banned_genLs):
                matches.append(i)
    return matches


# get list of ingredient names from ingredients list
def get_ingredient_name(ing_lst):
    result = []
    for i in ing_lst:
        result.append(i.name)
    result.sort() # sort them alphabetically
    return result

# get list of recipe names from recipes list
def get_recipe_name(rec_lst):
    result = []
    for i in rec_lst:
        result.append(i[1].title())
    return result

# get recipe index from name
def recipe_index(recipe_name):
    ind = -1
    for i in recipes:
        ind += 1
        if recipe_name == i[1].title():
            return ind
    return KeyError

# returns a string of the ingredients of a recipe
def get_ingredient_list(rec):
    result = ''
    ind = -1
    for i in rec[1].ingredients():
        ind += 1
        if ind > 0:
            result += '\n' + i
        else:
            result += i
    return result

# makes a new window showing all of the allergens in the current recipe
def display_allergens(rec):
    allergens_str = '' # this builds up a long string of all the allergens based on the ingredient
    for ing in rec[0]:
        update_allergens(ing)
        if len(allergens_str) > 0:
            allergens_str += '\n'
        allergens_str += ing.name + ': '
        ind = -1
        for i in ing.allergens:
            ind += 1
            if ind > 0:
                allergens_str += ', ' + i
            else:
                allergens_str += i
    layout = [
            [gui.Text(rec[1].title() + ' allergens',font=(16))],
            [gui.Text(allergens_str)],
            [gui.Button('Close',key='-CLOSE-')]
        ]
    window = gui.Window('allergens',layout,size=(400,300),element_justification='center',margins=(6,20))
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == '-CLOSE-': # when window closes
            break
    window.close()
    
# initializing menu definitions for the GUI    
ingredient_menu_def = ['Ingredient', get_ingredient_name(ingredient_list)]
genLs_menu_def = ['GenL', get_ingredient_name(genL_list)]
recipe_menu_def = ['Recipe', get_recipe_name(recipes)]

# initialize the ingredient list for menu_def (GUI stuff)
ing_lst = ''
ind = -1
for i in recipes[0][1].ingredients():
    ind += 1
    if ind > 0:
        ing_lst += '\n' + i
    else:
        ing_lst += i

# initialize the instructions list for recipes (GUI stuff)
ins_lst = ''
ind = -1
for i in recipes[0][1].instructions_list():
    ind += 1
    if ind > 0:
        ins_lst += '\n' + i
    else:
        ins_lst += i

# window's layout design
layout_top = [  [gui.Text("Recipe Project",font=(18))]]

layout_middle_top = [gui.Column([[gui.ButtonMenu('Ingredient Info',menu_def=ingredient_menu_def,border_width=5,key='-DISPLAY-INGREDIENT-')]]),
                     gui.Column([[gui.ButtonMenu('GenLs Info',menu_def=genLs_menu_def,border_width=5,key='-DISPLAY-GENL-')]]),
                     gui.Column([[gui.Button('Add Ingredient',key='-ADD-INGREDIENT-')]]),
                     gui.Column([[gui.Button('Add GenL',key='-ADD-GENL-')]])]
            
layout_middle = [  [gui.Text("What recipe would you like?"),
                    gui.ButtonMenu('Recipes',menu_def=recipe_menu_def,border_width=5,key='-RECIPE-',visible=True)]]

layout_middle_bottom = [[gui.Text(recipes[0][1].title(),key='-RECIPE-TITLE-')],
                        [gui.Text('Ingredients')],
                        [gui.Text(ing_lst,key='-INGREDIENT-LIST-')],
                        [gui.Button('Visit Website for More Info',key='-WEBSITE-')]]

layout_bottom = [   [gui.Text('',key='-STATUS-')],
                    gui.Column([[gui.Button('Display Allergens',key='-DISPLAY-ALLERGENS-')]]),
                    gui.Column([[gui.Button('Request Substitution',key='-SUBSTITUTION-')]]),
                    gui.Column([[gui.Button('GitHub',key='-GITHUB-')]]),
                    gui.Column([[gui.Button('Close',key='-CLOSE-')]])
]

layout = [
    [   
        layout_top,
        layout_middle_top,
        layout_middle,
        layout_middle_bottom,
        layout_bottom
    ]
]

# window creation
window = gui.Window('Recipe Project', layout,size=(750,600),element_justification='center')

# event loop
def win_run():
    # active recipe
    # default to first recipe
    active_recipe = recipes[0]
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == '-CLOSE-': # when window closes
            break
        elif event == '-DISPLAY-INGREDIENT-': # when the user wants to display an ingredient
            selection = values[event] # get name of ingredient
            window['-STATUS-'].update('Displayed info for ingredient: ' + selection + '.')
            show_ing(selection) # display ingredient info in new window
        elif event == '-DISPLAY-GENL-': # when the user wants to display a genL
            selection = values[event] # get name of genL
            window['-STATUS-'].update('Displayed info for genL: ' + selection + '.')
            show_genL(selection) # display genL info in new window
        elif event == '-ADD-INGREDIENT-': # when the user wants to add a new ingredient to the database
            window['-STATUS-'].update('Opened the window to add an ingredient.')
            test = add_ingredient()
            window['-DISPLAY-INGREDIENT-'].update(menu_definition=['Ingredient', get_ingredient_name(ingredient_list)])
            if test:
                window['-STATUS-'].update('Added ingredient.')
            else:
                window['-STATUS-'].update('Canceled adding ingredient.')
        elif event == '-ADD-GENL-': # when the user wants to add a new ingredient to the database
            window['-STATUS-'].update('Opened the window to add a genL.')
            test = add_genL()
            window['-DISPLAY-GENL-'].update(menu_definition=['GenL', get_ingredient_name(genL_list)])
            if test:
                window['-STATUS-'].update('Added genL.')
            else:
                window['-STATUS-'].update('Canceled adding genL.')
        elif event == '-RECIPE-': # when the user changes the recipe
            selection = values[event] # get name of new recipe
            window['-RECIPE-TITLE-'].update(selection) # update recipe title display
            active_recipe = recipes[recipe_index(selection)] # update active recipe
            active_ingredients = get_ingredient_list(active_recipe) # get ingredients string
            window['-INGREDIENT-LIST-'].update(active_ingredients) # update displayed ingredients
            window['-STATUS-'].update('Changed the recipe.')
        elif event == '-WEBSITE-': # when the user wants to open the recipe online
            url = active_recipe[2]
            webbrowser.open(url)
            window['-STATUS-'].update('Opened the recipe online.')
        elif event == '-DISPLAY-ALLERGENS-': # when the user wants to display the allergies present in the current recipe
            window['-STATUS-'].update('Displayed the allergens associated with the recipe.')
            display_allergens(active_recipe)
        elif event == '-SUBSTITUTION-': # when the user wants to substitute a food
            substitute(active_recipe)
            window['-STATUS-'].update('Opened the substitution window.')
        elif event == '-GITHUB-': # when the user clicks on the GitHub button
            webbrowser.open('https://github.com/Mj3399/contributors-El-Mj-Recipe-Planner-KRR-Project')
            window['-STATUS-'].update('Opened the GitHub repository.')
    window.close()

def main():
    print()
    win_run()

if __name__ == "__main__":
    main()
