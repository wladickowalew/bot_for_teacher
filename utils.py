from aiogram.utils.helper import Helper, HelperMode, ListItem

class OperationStates(Helper):
	mode = HelperMode.snake_case

	WAIT_FIRST_NUMBER_STATE = ListItem()
	WAIT_OPERATION_STATE = ListItem()
	WAIT_SECOND_NUMBER_STATE = ListItem()