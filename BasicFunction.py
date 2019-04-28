#!/user/bin/python3
# -*-coding:UTF-8-*-
def main(beanName, entityName, viewName, mapperName):
    add(entityName, mapperName)
    addList(entityName, mapperName)
    modify(entityName, mapperName)
    remove(mapperName)
    removeList(mapperName)


def add(entityName, mapperName):
    print("@Override\n"
          + "public Boolean add(" + entityName + " model) {\n"
          + "\tif (model == null)\n"
          + "\t\treturn false;\n"
          + "\treturn " + mapperName + ".insert(toBean(model)) > 0;\n"
          + "}")


def addList(entityName, mapperName):
    print("@Override\n"
          + "public Boolean add(List<" + entityName + "> models) {\n"
          + "\tif (models == null || models.isEmpty())\n"
          + "\t\treturn false;\n"
          + "\tboolean b = true;\n"
          + "\tfor (" + entityName + " model : models)\n"
          + "\t\tb &= add(model);\n"
          + "\treturn b;\n"
          + "}")


def modify(entityName, mapperName):
    print("@Override\n"
          + "public Boolean modify(" + entityName + " model) {\n"
          + "\tif (model == null)\n"
          + "\t\treturn false;\n"
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
          + "\tif (ids == null || ids.isEmpty())\n"
          + "\t\treturn false;\n"
          + "\tboolean b = true;\n"
          + "\tfor (String id : ids)\n"
          + "\t\tb &= remove(id);\n"
          + "\treturn b;\n"
          + "}")


if __name__ == "__main__":
    """
    entityName:实体名
    mapperName:mapper名
    """
    entityName = "StorageApply"
    mapperName = "storageApplyBeanMapper"
    main(entityName + "Bean", entityName, entityName + "View", mapperName)
