from behave import given, when, then
from pages.page import SymptomatePage


@given("I am on the {language_code} version of the Symptomate")
def go_to_the_symptomate_page(context, language_code):
    SymptomatePage(context.driver, context.wait).open(language_code)


@when("I change language using dropdown menu on {language_code}")
def change_language_using_dropdown(context, language_code):
    SymptomatePage(context.driver, context.wait).change_language(language_code)


@then("I am on the {language_code} version of the Symptomate")
def is_correct_language(context, language_code):
    SymptomatePage(context.driver, context.wait).is_correct_language(language_code)
