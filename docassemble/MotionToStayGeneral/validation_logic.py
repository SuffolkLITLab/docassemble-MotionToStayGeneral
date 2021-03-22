from docassemble.base.util import validation_error

def determine_docket_number_J_P(docket_number):
  if 'J' in docket_number.upper():
    validation_error('There should not be a J in your docket number. Select "Yes" above and continue.')
    
  return True