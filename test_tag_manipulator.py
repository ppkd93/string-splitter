from tag_manipulator import TagManipulator

def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult

def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


# "java" must return ["java"]
def test_split_comma_java_string_result_java_array():
    # arrange
    stringToSplit = "java"
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


# "java, python" must return ["java", "python"]
# " java" must return ["java"]
# ",java" must return ["java"]
# "java," must return ["java"]
# "java byte code, python" must return must return ["java byte code", "python"]