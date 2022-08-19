# shop
To create a MongoDB and connect to python app to store and calculate, bill details, items sold, item prices ect

module1:
1-->store all items along with price in a collection

module2:
1-->selection of user(it is a billing person or the store manager)
2-->if it is a billing person
   1-->take item inputs(user phone number(id),item and the quantity(kilograms))
   2-->the billing person should be able to take further inputs
   3-->after the purchase order is done bill should be generated with total value(store name,date and time,bill number)
   4-->the details should be stored in a new collection()
   
module3:
1-->the admin should have option to the summary
 1-->summay based on the amount-rupees(on that day based on items)-EOD
 2-->summary based on the  items quantity-EOD
 3-->summary or statement for a particular period(amount based or quantity based)-optional
