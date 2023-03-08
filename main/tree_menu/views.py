from django.shortcuts import render
from .models import Folder


def home(request):
    return render(request, 'tree_menu/main_menu.html')


def get_context(request, menuName, id=None):
    '''
    Display "Main menu"
    '''

    if id is None:
        context = {'mainMenu': Folder.objects.filter(menu__name=menuName, parent=None),
                    'name': menuName}
        # return render(request, 'tree_menu/menu_tree.html', context)
        return context
    base = Folder.objects.filter(menu__name=menuName)

    def append_children(to, _from):
        '''
        Append children from "_from" variable into the "to" variable and return it
        '''
        if type(_from) != int:
            children = to
            for child in children: 
                if child.id == _from.id:
                    child.children = _from.children
            to.children = children
        return to

    def tree(childrenFolder):
        '''
        Recursively find all menus above the selected one and
        display them along with children of the selected menu
        as well as neighbors of the higher folders
        '''
        grandID = childrenFolder if type(childrenFolder) == int else childrenFolder.parent.id

        selectedField = base.get(id=grandID) # The selected folder
        selectedField.children = base.filter(parent=grandID) \
              if base.filter(parent=grandID) else [] # Find children of the selected folder

        append_children(to=selectedField.children, _from=childrenFolder)

        if not selectedField.parent:
            return selectedField
        return tree(childrenFolder=selectedField)

    context = {
        'mainMenu': append_children(to=base.filter(parent=None), _from=tree(childrenFolder=id)),
        'name': menuName
        }
    # return render(request, 'tree_menu/menu_tree.html', context)
    return context


def main_menu(request, menuName, id=None):
    return render(
        request, 
        'tree_menu/menu_tree.html', 
        get_context(request=request, menuName=menuName, id=id)
    )