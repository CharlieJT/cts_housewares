<h1 align="center">
CT's Housewares - Testing
</h1>

<div align="center">

[**Main README.md file**](README.md)

[CT's Housewares](https://cts-housewares.herokuapp.com/)
</div>

## Contents Table

1. [**Automated Testing**](#automated-testing)
    - [**Validating Code**](#validating-code)
    - [**Python Testing**](#python-testing)

2. [**User Stories Testing**](#user-stories-testing)

3. [**Manual Testing**](#manual-testing)
    - [**Testing on Desktop**](#testing-on-desktop)
    - [**Testing on tablet and mobile devices**](#testing-on-tablet-and-mobile-devices)
4. [**Bugs Found**](#bugs-found)
    - [**Bugs Solved**](#bugs-solved)
    - [**Bugs Unsolved**](#bugs-unsolved)
5. [**Further Testing**](#further-testing)
<br>

## Automated Testing

### Validating Code

Validation services were used to ensure that code was valid code used to develop the website.

- [W3C Markup Validation Service](https://validator.w3.org/) was used to test HTML code to ensure it was valid code.
I needed to remove jinja to ensure this first.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to test CSS code to ensure it was valid code.
- [Code Beautify JavaScript Validator](https://codebeautify.org/jsvalidate) was used to test JavaScript code to ensure it was valid code.

### Django Testing

Django testing was implemented into the project to test to ensure that the business logic of the project was all working as intended.

As this was the first time, I was doing Django testing, I decided to do my testing after writing my code.
As it wasn't possible to tests every single function in my app.py, I tested around 80% of my functionality using the Pareto Principle.

An import called 'TestCase' was used to carry out the testing.

The functions that were tested were as follows:

- Home App
    - Models
    - Views
- Product App
    - Models
    - URLs
    - Views
- Search App
    - URLs
- Checkout App
    - Forms
    - Models
    - URLs
    - Views
- Account App
    - Forms
    - URL's

A total of 35 tests were run & all were passing.

## User Stories Testing

- ### As a user, I'd like to see:
    - ### A professional and strong looking website to draw the user into using the website.
        - Banners & images have been made to look professional to draw the user in.
        - Bootstrap was used as a CSS framework to help with layout & styling & include features such as navbars, accordions, buttons.
        - Font Awesome icons were used to give buttons & links a better indication of their purpose.
        - A colour template was adhered to give it a more styled look.
        - Pagination was included to help separate products & also helps with loading time.
        - A progress bar was added to the cart, checkout & successful payment pages to give the user an indication of how far they are through the payment process.
    - ### Navigations which are simple & informative which don't leave the user unsure of how to get to the page they want to get to.
        - You will find a navigation link on every page of the website.
        - The CT's Housewares will navigate you back to the home page.
        - Breadcrumbs have been added to all pages which are necessary to jump back to specific pages with the name of the page that is linked this helps a lot with the website navigation.
    - ### Images of the products that are available on the website as soon as a user goes to the website.
        - Banners have been included in a carousel on the home page which you can click left or right to views, also when you click the image, it will take your to the products with that specific brand.
    - ### Buttons which are simple but informative & give a good indication of their purpose.
        - Buttons have been labelled correctly with their accordance.
        - They have been given the appropriate colour for either purpose.
        - Icons have been added to most of the button to give a better indication of their purpose.
    - ### Subtle animations to not overcomplicate the website, but to give a strong professional look & feel.
        - A back to top chevron has a nice animation when you hover over it, it will transform to blue from white & rotate.
        - A side drawer animation is given when the user clicks on the burger icon on mobile display, the burger icon will transform into a times symbol & the side drawer will slide into vision when clicked & a backdrop will appear over the background. When the backdrop is clicked or when the times' symbol is clicked, the side drawer will slide back out of vision & the times' symbol will transform back to a burger icon.
        - An Image slider has been included on the individual product page so that the user can choose between images they would like to see more of. Also when the main image is hovered over, it will zoom in on the image so the user can get a better look at the image.
    - ### Icons that give the user a better indication of what their specific action is.
        - Icons have been added to most of the button to give a better indication of their purpose.
        - Icons have been added to each of the links in the navbar to give a better indication of their purpose.
    - ### I have all of the relevant information given to me at the appropriate time.
        - When a user is not logged in, they will see Cart, Login & Register in the top right-hand corner & when a user is logged in, they will see Cart, Profile & Logout in the top right-hand corner.
        - Login & Registration pages will not be able to be viewed when the user is logged in & profile, the checkout will not be able to be viewed when a user is logged out.

## Manual Testing

A number of manual tests were done to ensure the website was working with its intended purpose and use.

### Testing on Desktop

The website was tested numerous times in Browsers: Chrome, Safari, Firefox and Internet Explorer
on a Laptop, Macbook & Desktop PC.

#### 1. Dashboard

I checked that:

- There is no upwards chevron in the bottom right-hand corner until the page has been scrolled down.
- The Favicon is loading correctly.
- The upwards chevron is appearing when scrolled down the page & that it's animating correctly when hovered over
& when it's clicked.
- The navbar is correctly animating so the main logo is decreasing in size when scrolled down.
- The footer was properly sitting at the bottom of the page as I added a sticky footer to the bottom.
- The navbar search bar is working correctly.
- A notification will show up next to the cart link if there are 1 or more items in the cart.

#### 2. Home Page

I checked that:

- The brand carousel is loading properly, is 100 view width & there are no issues with the height or width.
- Each Carousel is responsive & changes depending on which display the user is looking at the website.
- Each Carousel item is linking correctly to their respective brand on the products page.

#### 3. Product Page

I checked that:

- All links are working in the breadcrumb.
- Data is coming through & is only showing 12 items per page.
- Ensure Pagination is working correctly & clicking between pages is working, the active page is coloured blue, previous & the first page is not being shown on the first page & the next & last page is not being shown on the last page.
- Images & data are sitting correctly in their brand card.
- "Item out of stock" is being shown on the product card when the stock is 0.
- If a brand is selected, the brand is active in the select brand dropdown.
- The select brand drop down is working correctly & when selected, you will start back at page 1.
- When an item is added to the cart, you are notified.
- When an item that is already in the cart is added to the cart, it will add the extra items to your current cart items & you will be notified.
- You cannot add more stock than what is in stock.
- If you have an item in the cart & you add more to it & the total of the amount in the cart & the amount you have added comes to more than the stock, it won't let you add it to the cart & you will be notified.
- All items are shown if the URL is `/product`.
- The page at the top of the page matches the active page in pagination.
- The total amount of items plus the query is shown at the top of the page.
- Search/Brand query does not interfere with pagination functionality.
- There is a hover effect when hovering over each of the product cards.
- Images & product descriptions are links to the individual page of that particular product.

#### 4. Individual Product Page

I checked that:

- All links are working in the breadcrumb.
- Product slider is picking all of the relevant images & each one is sliding correctly.
- Is there is only 1 image, it will not show that image below.
- Images are zooming correctly & even working when the mouse is moved.
- "Item out of stock" is being shown on the product card when the stock is 0.
- When an item is added to the cart, you are notified.
- When an item that is already in the cart is added to the cart, it will add the extra items to your current cart items & you will be notified.
- You cannot add more stock than what is in stock.
- If you have an item in the cart & you add more to it & the total of the amount in the cart & the amount you have added comes to more than the stock, it won't let you add it to the cart & you will be notified.
- The Tab is working correctly & clicking each of the section headings takes you to that section.

#### 5. Login Page

I checked that:

- All links are working in the breadcrumb.
- All fields are sitting correctly on the page.
- All required fields are shown with an asterisk.
- All fields must be filled in before the user can successfully log in.
- The correct credentials must be entered for the user to successfully log in & if at any time the user is unable to log in, the user will be notified.
- If a user successfully logs in, they are taken back to the home page & notified that they are logged in.
- Links to the registration & the forgotten password pages are working correctly.

#### 6. Registration Page

I checked that:

- All links are working in the breadcrumb.
- All fields are sitting correctly on the page.
- All required fields are shown with an asterisk.
- All fields must be filled in before the user can successfully register.
- The correct credentials must be entered for the user to successfully register & if, at any time the user is unable to register, the user will be notified.
- If a user successfully registers, they are taken back to the home page & notified that they have successfully registered & are logged in.
- Links to the login page is working correctly.

#### 7. Cart Page

I checked that:

- All links are working in the breadcrumb.
- When there are no items in the cart & the user is not logged, it will say there are no items & ask you to log in to checkout.
- When there are no items in the cart & the user is logged in, it will say that there is no item to checkout.
- When there are items in the cart & a user is not logged in, no progress bar is shown & you will not be able to go to checkout.
- When there are items in the cart & a user is logged in, a progress bar will be shown & you will be allowed to check out your items, the progress bar will only show the first circle highlighted.
- When amending the quantity of an item, you first change the quantity & then click the button to update your cart & update the correct item.
- When you click the remove button, it will remove the correct item from the cart.
- Everything sitting correctly on the page.

#### 8. Checkout Page

I checked that:

- Page can only be accessed if a user is logged in. If not, they will be navigated to the login page.
- All links are working in the breadcrumb.
- All fields are sitting correctly on the page.
- All required fields are shown with an asterisk.
- All required fields must be filled in before the user can successfully submit payment.
- The correct credentials must be entered for the user to successfully pay & if, at any time the user is unable to pay, the user will be notified.
- If a user successfully pays, they are taken to the successful payment page.
- A progress bar will be shown which will only show the first & second circle being highlighted.

#### 9. Successful Payment Page

I checked that:

- Page can only be accessed if a user is logged in. If not, they will be navigated to the login page.
- All links are working in the breadcrumb.
- A progress bar will be shown which will only show all of the circles being highlighted.
- Navigation to the profile page works & that the order has successfully been updated.
- The select brand drop down is working correctly & when selected, it will navigate you to the product page with the correct brand & you will start back at page 1.
- Link back to the home page is working.

#### 10. Profile Page

I checked that:

- Page can only be accessed if a user is logged in. If not, they will be navigated to the login page.
- All links are working in the breadcrumb.
- All information is coming through, Username, Name, Email Address & Account Created.
- If a user has no orders, the order history section will not be shown.
- If a user has made at least 1 order, the order history section will be shown with the correct date(s) & time(s).
- When you click on one of the order history accordion items, it will show you the complete order with the correct information.


### Testing on Tablet & Mobile

The website was tested on iPhone 6, iPhone 8 Plus through Chrome and Safari. It's also been run through Chrome Developer tools
in the 'Responsive' setting changing the width and height and changed to each device setting.

#### 1. Dashboard

I checked that:

- There is no upwards chevron in the bottom right-hand corner until the page has been scrolled down.
- The upwards chevron is appearing when scrolled down the page & that it's animating correctly when hovered over
& when it's clicked.
- The navbar is correctly animating so the main logo is decreasing in size when scrolled down.
- Side drawer is properly sliding out & burger icon/close icon is properly animating.
- The footer was properly sitting at the bottom of the page as I added a sticky footer to the bottom.
- The side drawer search bar is working correctly.
- A notification will show up next to the cart link in the side drawer if there are 1 or more items in the cart.

#### 2. Home Page

I checked that:

- The brand carousel is loading properly, is 100 view width & there are no issues with the height or width.
- Each Carousel is responsive & changes depending on which display the user is looking at the website.
- Each Carousel item is linking correctly to their respective brand on the products page.

#### 3. Product Page

I checked that:

- All links are working in the breadcrumb.
- Data is coming through & is only showing 12 items per page.
- Ensure Pagination is working correctly & clicking between pages is working, the active page is coloured blue, previous & the first page is not being shown on the first page & the next & last page is not being shown on the last page.
- Images & data are sitting correctly in their brand card.
- "Item out of stock" is being shown on the product card when the stock is 0.
- If a brand is selected, the brand is active in the select brand dropdown.
- The select brand drop down is working correctly & when selected, you will start back at page 1.
- When an item is added to the cart, you are notified.
- When an item that is already in the cart is added to the cart, it will add the extra items to your current cart items & you will be notified.
- You cannot add more stock than what is in stock.
- If you have an item in the cart & you add more to it & the total of the amount in the cart & the amount you have added comes to more than the stock, it won't let you add it to the cart & you will be notified.
- The page at the top of the page matches the active page in pagination.
- The total amount of items plus the query is shown at the top of the page.
- Search/Brand query does not interfere with pagination functionality.
- There is a hover effect when hovering over each of the product cards.
- Images & product descriptions are links to the individual page of that particular product.

#### 4. Individual Product Page

I checked that:

- All links are working in the breadcrumb.
- Product slider is picking all of the relevant images & each one is sliding correctly.
- Is there is only 1 image, it will not show that image below.
- Images are zooming correctly & even working when the mouse is moved.
- "Item out of stock" is being shown on the product card when the stock is 0.
- When an item is added to the cart, you are notified.
- When an item that is already in the cart is added to the cart, it will add the extra items to your current cart items & you will be notified.
- You cannot add more stock than what is in stock.
- If you have an item in the cart & you add more to it & the total of the amount in the cart & the amount you have added comes to more than the stock, it won't let you add it to the cart & you will be notified.
- The tab is working correctly & clicking each of the section headings takes you to that section.

#### 5. Login Page

I checked that:

- All links are working in the breadcrumb.
- All fields are sitting correctly on the page.
- All required fields are shown with an asterisk.
- All fields must be filled in before the user can successfully log in.
- The correct credentials must be entered for the user to successfully log in & if at any time the user is unable to log in, the user will be notified.
- If a user successfully logs in, they are taken back to the home page & notified that they are logged in.
- Links to the registration & the forgotten password pages are working correctly.

#### 6. Registration Page

I checked that:

- All links are working in the breadcrumb.
- All fields are sitting correctly on the page.
- All required fields are shown with an asterisk.
- All fields must be filled in before the user can successfully register.
- The correct credentials must be entered for the user to successfully register & if, at any time the user is unable to register, the user will be notified.
- If a user successfully registers, they are taken back to the home page & notified that they have successfully registered & are logged in.
- Links to the login page is working correctly.

#### 7. Cart Page

I checked that:

- All links are working in the breadcrumb.
- When there are no items in the cart & the user is not logged, it will say there are no items & ask you to log in to checkout.
- When there are no items in the cart & the user is logged in, it will say that there is no item to checkout.
- When there are items in the cart & a user is not logged in, no progress bar is shown & you will not be able to go to checkout.
- When there are items in the cart & a user is logged in, a progress bar will be shown & you will be allowed to check out your items, the progress bar will only show the first circle highlighted.
- When amending the quantity of an item, you first change the quantity & then click the button to update your cart & update the correct item.
- When you click the remove button, it will remove the correct item from the cart.
- Everything sitting correctly on the page.

#### 8. Checkout Page

I checked that:

- Page can only be accessed if a user is logged in. If not, they will be navigated to the login page.
- All links are working in the breadcrumb.
- All fields are sitting correctly on the page.
- All required fields are shown with an asterisk.
- All required fields must be filled in before the user can successfully submit payment.
- The correct credentials must be entered for the user to successfully pay & if, at any time the user is unable to pay, the user will be notified.
- If a user successfully pays, they are taken to the successful payment page.
- A progress bar will be shown which will only show the first & second circle being highlighted.

#### 9. Successful Payment Page

I checked that:

- Page can only be accessed if a user is logged in. If not, they will be navigated to the login page.
- All links are working in the breadcrumb.
- A progress bar will be shown which will only show all of the circles being highlighted.
- Navigation to the profile page works & that the order has successfully been updated.
- The select brand drop down is working correctly & when selected, it will navigate you to the product page with the correct brand & you will start back at page 1.
- Link back to the home page is working.

#### 10. Profile Page

I checked that:

- Page can only be accessed if a user is logged in. If not, they will be navigated to the login page.
- All links are working in the breadcrumb.
- All information is coming through, Username, Name, Email Address & Account Created.
- If a user has no orders, the order history section will not be shown.
- If a user has made at least 1 order, the order history section will be shown with the correct date(s) & time(s).
- When you click on one of the order history accordion items, it will show you the complete order with the correct information.

## Bugs Found

### Bugs Solved

1. #### Issues with brand string & search string.

    A string needed to be added to the url depending whether you were doing a search or you were doing a brand query.
    
    **How it was fixed**:

    - To get around this issue, i set a variable to check whether brand was true, if so then I set a variable with the correct string, if not then I set the string to empty.

    ``` python
    brand = request.GET.get('brand', '')
    if brand:
        products = Product.objects.filter(Q(brand__icontains=brand))
        page_request_var = "brand={}&".format(brand)
    else:
        products = Product.objects.all()
        page_request_var = ''
    ```

2. #### Getting cart to update without going over the stock count.

    When an item was in the cart & you wanted to update the cart, with the way it's currently working it will add the amount requested to the currently total quantity of that item. You will only let you to add as many items there are in stock to the cart but it did not do a check to see if there were items already in the cart. 
    
    **How it was fixed**:

    - To get around this issue, I did a check to make sure that the quantity of the item which was already in the cart plus the amount of items that were requested to put in the basket did not go over the amount of items there are of that product in stock, if so, then an error will occur.

    ``` python
    def add_to_cart(request, id):
    """ This will add a specific product to the basket """
    quantity=int(request.POST.get('quantity'))
    
    product = get_object_or_404(Product, pk=id)
    id = str(id)

    cart = request.session.get('cart', {})
    if cart.get(id, None):
        if cart[id] + quantity > product.stock:
            messages.error(request, "Unable to add an extra '{}' of this item to your cart as it will exceed the number of stock!".format(quantity)) 
        else:
            cart[id] = int(cart[id]) + quantity
            messages.success(request, "Added '{}' extra item(s) of '{}' to your cart!".format(quantity, product.description)) 
    else:
        cart[id] = cart.get(id, quantity)
        messages.success(request, "Added '{}' item(s) of '{}' to your cart!".format(quantity, product.description))

    request.session['cart'] = cart
    ```

### Bugs Unsolved

1. #### Smooth scrolling in Safari not working.

    When in safari, smooth scrolling does not work when clicking on the upwards chevron & the
    downwards chevron.
    
    Unfortunately, I could not figure a way around this issue. I tried searching the internet, but
    I couldn't find the answer.
    
2. #### Glitchy upwards chevron.

    At times, the upwards chevron can become glitchy & will animate on click instead of hover.
    
    I did try to look for the answer to this, but I didn't see this as a major issue as the
    chevron was still working as it should.
    
3. #### Progress Bar showing up ugly in mobile.

    At times, the progress bar will show up ugly on mobile devices such as Apple devices.

    I tried looking for the answer & I also asked on slack to see if somebody had the answer but nobody could find the answer to the issue.

4. #### Clicking back when you are on an individual product.

    When you click into a product individual page & add an item to the cart, you will have to do a double click on the breadcrumb to take you back to where you were on the product page.

    I tried looking for the answer to see if there was an option to take you back to the page you were on previously, being on the correct page on pagination but I, unfortunately, could not find the answer.

## Further Testing

- Friends, family and fellow students were asked to check the website on all devices they had, they tested functionality and layout, positive and constructive criticism was provided.
- Tested in Chrome DevTools on all different devices and by scrolling up and down in the responsive setting.    