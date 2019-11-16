# Created by zzohamadro at 10/23/19
Feature: Test for product  selection
  # Enter feature description here

  Scenario: User can loop through dress colors
    Given Open Amazon product B07K16Z8LH page
    Then Verify User can select through colors

  Scenario: User can navigate through product colors
    Given Open Amazon product B07BKD8JCQ page
    Then Verify User can loop through colors


   Scenario: Size tooltip is shown upon hovering over Add To Cart button
     Given Open Amazon product B074TBCSC8 page
     When Hover over Add To Cart button
     Then Verify size selection tooltip is shown


   Scenario: User can select Books department
     Given Open Amazon page
     When Select Books Department
     And Search for Faust
     Then Books department is selected

   Scenario: User can search for a product in Sports & Outdoors department
     Given Open Amazon page
     When Select Sports & Outdoors Department
     Then Sports & Outdoors department is selected
     When Search for camping tents
     Then Sports & Outdoors department is selected

   Scenario: Mega menu deals is shown upon hovering over Sales and Deals link
      Given Open Amazon product B074TBCSC8 page
      When Hovering over Sales and Deals link
      Then Verifies user sees the mega menu deals

