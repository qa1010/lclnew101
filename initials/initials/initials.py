def get_initials(fullname):
    
    name_list = fullname.split()
    init = ''
    for name in name_list:
      init = init + name[0]

    cap = init.upper()
    return(cap)

