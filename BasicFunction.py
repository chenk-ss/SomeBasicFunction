#!/user/bin/python3
# -*-coding:UTF-8-*-
def main(beanName, entityName, viewName, mapperName):
    query(mapperName, viewName)
    print("\n")
    add(entityName, mapperName)
    print("\n")
    addList(entityName, mapperName)
    print("\n")
    modify(entityName, mapperName)
    print("\n")
    remove(mapperName)
    print("\n")
    removeList(mapperName)
    print("\n")
    page(viewName, beanName)
    print("\n")
    queryList(viewName)
    print("\n")
    setParam()
    print("\n")
    setPage()
    print("\n")
    toBean(beanName, entityName)
    print("\n")
    toView(beanName, viewName)
    print("\n")
    toViewList(beanName, viewName)
    print("\n")
    serviceInterface(beanName, entityName, viewName)


def query(mapperName, viewName):
    print("@Override\n"
          + "public " + viewName + " query(String id) {\n"
          + "\tif (id == null || \"\".equals(id)){\n"
          + "\t\treturn null;\n\t}\n"
          + "\treturn toView(" + mapperName + ".selectByPrimaryKey(id));\n"
          + "}")


def add(entityName, mapperName):
    print("@Override\n"
          + "public Boolean add(" + entityName + " model) {\n"
          + "\tif (model == null) {\n"
          + "\t\treturn false;\n\t}\n"
          + "\treturn " + mapperName + ".insert(toBean(model)) > 0;\n"
          + "}")


def addList(entityName, mapperName):
    print("@Override\n"
          + "public Boolean add(List<" + entityName + "> models) {\n"
          + "\tif (models == null || models.isEmpty()) {\n"
          + "\t\treturn false;\n\t}\n"
          + "\tboolean b = true;\n"
          + "\tfor (" + entityName + " model : models) {\n"
          + "\t\tb &= add(model);\n\t}\n"
          + "\treturn b;\n"
          + "}")


def modify(entityName, mapperName):
    print("@Override\n"
          + "public Boolean modify(" + entityName + " model) {\n"
          + "\tif (model == null) {\n"
          + "\t\treturn false;\n\t}\n"
          + "\treturn " + mapperName + ".updateByPrimaryKeySelective(toBean(model)) > 0;\n"
          + "}")


def remove(mapperName):
    print("@Override\n"
          + "public Boolean remove(String id) {\n"
          + "\treturn " + mapperName + ".deleteByPrimaryKey(id) > 0;\n"
          + "}")


def removeList(mapperName):
    print("@Override\n"
          + "public Boolean remove(List<String> ids) {\n"
          + "\tif (ids == null || ids.isEmpty()) {\n"
          + "\t\treturn false;\n\t}\n"
          + "\tboolean b = true;\n"
          + "\tfor (String id : ids) {\n"
          + "\t\tb &= remove(id);\n\t}\n"
          + "\treturn b;\n"
          + "}")


def page(viewName, beanName):
    print("@Override\n"
          + "public PageData<"+viewName+"> page(Integer start, Integer limit, String sort, QueryParam query) {\n"
          + "\tPageData<" + viewName + "> pageData = new PageData<>();\n"
          + "\tList<" + beanName + "> bList = " + mapperName + ".selectByPageWithExample(setPage(start, limit, sort, setParam(query)));\n"
          + "\tList<" + viewName + "> vList = toView(bList);\n"
          + "\tInteger count = " + mapperName + ".countByExample(setPage(start, limit, sort, setParam(query)));\n"
          + "\tpageData.setDatas(vList);\n"
          + "\tpageData.setTotal(count);\n"
          + "\treturn pageData;\n"
          + "}")


def queryList(viewName):
    print("@Override\n"
          + "public List<" + viewName + "> query(QueryParam query) {\n"
          + "\treturn toView(" + mapperName + ".selectByExample(setParam(query)));\n"
          + "}")


def setParam():
    print("@Override\n"
          + "public BaseExample setParam(QueryParam query) {\n"
          + "\treturn null;\n"
          + "}")


def setPage():
    print("@Override\n"
          + "public BaseExample setPage(Integer start, Integer limit, String sort, BaseExample example) {\n"
          + "\treturn null;\n"
          + "}")


def toBean(beanName, entityName):
    print("@Override\n"
          + "public " + beanName + " toBean(" + entityName + " entity) {\n"
          + "\tif(entity == null) {\n"
          + "\t\treturn null;\n\t}\n"
          + "\t" + beanName + " bean = new " + beanName + "();\n"
          + "\treturn bean;\n"
          + "}")


def toView(beanName, viewName):
    print("@Override\n"
          + "public " + viewName + " toView(" + beanName + " bean) {\n"
          + "\tif(bean == null) {\n"
          + "\t\treturn null;\n\t}\n"
          + "\t" + viewName + " view = new " + viewName + "();\n"
          + "\treturn view;\n"
          + "}")


def toViewList(beanName, viewName):
    print("@Override\n"
          + "public List<" + viewName + "> toView(List<" + beanName + "> beans) {\n"
          + "\tif(beans == null || beans.isEmpty()) {\n"
          + "\t\treturn null;\n\t}\n"
          + "\tList<" + viewName + "> views = new ArrayList<>();\n"
          + "\tfor (" + beanName + " bean : beans) {\n"
          + "\t\tviews.add(toView(bean));\n\t}\n"
          + "\treturn views;\n"
          + "}")


def serviceInterface(beanName, entityName, viewName):
    print(beanName + " toBean(" + entityName + " entity);")
    print(viewName + " toView(" + beanName + " bean);")
    print("List<" + viewName + "> toView(List<" + beanName + "> beans);")


if __name__ == "__main__":
    """
    entityName:实体名
    mapperName:mapper名
    """
    entityName = "VSpecialActivity"
    mapperName = "vSpecialActivityBeanMapper"
    main(entityName + "Bean", entityName, entityName + "View", mapperName)
