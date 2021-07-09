from send_email import extract_contacts, extract_summary, create_template, compose_email
import fire

def extract_contacts(contact_file):
  """
  Return two lists contacts, containing names and email addresses
  Please prepare an external files containing 2 information: name and email address
  Use the following format: <NAME> <EMAIL> on the flat file
  """
  names = []
  emails = []
  with open(contact_file, mode='r', encoding='utf-8') as contacts:
    for contact in contacts:
      names.append(' '.join(contact.split()[0:-1]))
      emails.append(contact.split()[-1])
  return names, emails
  # Export to Fire
  fire.Fire(debug)
