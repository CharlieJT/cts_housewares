<h1 align="center">
Full Stack Frameworks - Milestone Project 4 - CT's Housewares - Charlie Tipton
</h1>

<div align="center">
    <img src="https://i.ibb.co/gJybGW7/cts-housewares-layout.png" href="https://cts-housewares.herokuapp.com" target="_blank" alt="Responsive displays of CT's Housewares" border="0">
</div>

[![Build Status](https://travis-ci.org/CharlieJT/cts_housewares.svg?branch=master)](https://travis-ci.org/CharlieJT/cts_housewares)

[CT's Housewares](https://cts-housewares.herokuapp.com) is a website created for a user to purchase houseware products. It has been made so that the user can easily read & navigate around the website. Functionality has been added to allow purchasing a product quick & easy. Registration & log in has also been made simple & hassle-free along with information on user profile & order history. In addition to friendly colours, designs, alerts & animations, it makes a great website for purchasing products.

<br><br>
[**View CT's Housewares website here in Heroku!**](https://cts-housewares.herokuapp.com/)

1. [**UX**](#ux)
    - [**Project Purpose**](#project-purpose)
    - [**User Experience**](#user-experience)
    - [**User Stories**](#user-stories)
    - [**Design Ideas**](#design-ideas)
    - [**Wireframes**](#wireframes)
    - [**Developer and Business Purpose**](#developer-and-business-purpose)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

## UX

### Project Purpose

The goal of CT's Housewares is to give the user an easy & hassle-free experience when purchasing houseware products, ensuring that all actions are made as quick, simple & effective as possible such as:

- Registration
- Log in
- Profile Information
- Finding a product
- Viewing brands of a product
- Finding product information
- Viewing product images
- Adding products to the cart
- Adjusting the quantity of item(s) in cart
- Removing item(s) from cart
- Easy payment process
- Order History

### User Experience

- Users get a great sense of usability from the get-go. They are presented with a burger icon at the top of
the screen for mobile & tablet display & a navigation bar on desktop display for a Search bar, Products, Cart, Login & Registration.

- A Carousel of brands has been included so the user can see what products the website has to offer from the get-go, the images of are also clickable & will navigate you to the product page & showing their respective brand.

- All cards on the product page have a clickable image, title which will take them to an individual product page where they can see more about the product including more images, a brief description, brand, item number, specifications & dimensions.

- Breadcrumbs have been included at the top of specific pages to help easily navigate back to pages
they have previously come from.

- Asterisks (Star symbols) have been included in both registration & login fields to indicate which fields are required to be filled in before submission. If a user has submitted a form without filling in a required field, validation has been included & will prompt the user to input any input field that is required.

- Pagination has been included in the products page to keep data cleaner & to limit the amount of data shown at one time, this can help quite substantially with loading time if there are lots of products.

- When the delete button is clicked on the recipe page, the user is presented with a modal to ensure they want to
delete their recipe permanently.

- The user does not need to click a back button or to reload the page. Easy and informative buttons have always been provided to ensure the user has an easy way around the website.

- Log in & Registration has been implemented into the website to create a sense of security to the website.


### User Stories

- #### As a user, I'd like to see:
    - A professional and strong looking website to draw the user into using the website.
    - Navigations which are simple & informative which don't leave the user unsure of how to get to the page they want to get to.
    - Images of the products that are available on the website as soon as a user goes to the website.
    - Buttons which are simple but informative & give a good indication of their purpose.
    - Subtle animations to not overcomplicate the website, but to give a strong professional look & feel.
    - Icons that give the user a better indication of what their specific action is.
    - I have all of the relevant information given to me at the appropriate time.


### Design Ideas

The design of the website was to give a clean & intuitive look & feel ensuring the user gets the best experience along with appropriate & catching imagery to draw the user in to making a purchase.

- #### Fonts

    - The font **'Roboto'** was chosen as the primary font to ensure it had a professional look.

- #### Colours

    - <div style="background-color: #666666; width: 50px; height: 50px; border: 1px solid #000;"><div>
    <b>Hex Value: #666666;</b>

    This colour was used for the icons & text in the navbar.


    - <div style="background-color: #53a5e7; width: 50px; height: 50px; border: 1px solid #000;"><div>

   <b>Hex Value: #53a5e7;</b>

    This colour was used for the logo, the footer, the payment progress bar & some of the buttons throughout the website. It was also used to colour the back to top button when you hover over it.


    - <div style="background-color: #218838; width: 50px; height: 50px; border: 1px solid #000;"><div>

   <b>Hex Value: #218838;</b>

    This colour was used the "add to cart" button & the "checkout" button.


     - <div style="background-color: #ff0000; width: 50px; height: 50px; border: 1px solid #000;"><div>

   <b>Hex Value: #ff0000;</b>

    This is used for the text when an item is out of stock & also used for the notification of how many items there are in your cart.


    - <div style="background-color: #fff; width: 50px; height: 50px; border: 1px solid #000;"><div>

   <b>Hex Value: #fff;</b>

    This colour was used for the rest of the website including backgrounds & text when needed to contrast with backgrounds.
    
- #### Styling

    Styles have been made to give a professional, strong look. With the help of the CSS framework
    [Materialize!](https://materializecss.com/), I was able to implement a nice looking & well animated
    website without going over the top.
    
    **Special styles include:**
    
    - **Buttons** Buttons have been styled using bootstrap & colours have been picked using the bootstrap colour scheme.
    
    - **Pagination** Pagination consists of a "First Page" Button, "Previous Page" Button, "Next Page" Button, "Last Page" Button, "Current Page" Button & page numbers of pages if the page exists 2 before or 2 after Button. These have been styled so that the previous & first page indicator will not show is a user is on the first page & the last & next page indicators will not show if a user is on the last page. The previous & next page indicators have been styled grey with black text & the current page indicator has been styled blue with white text to give a better indicator of which page the user is currently on.
    
    - **Up chevron -** When a user scrolls 50 pixels down from the top of any page, an 'up' chevron will appear in the bottom left-hand corner of the screen. When hovered over on desktop, it will rotate 360° & border & chevron colour will change to blue. When clicked on mobile & tablet, it will perform the animation as the page is scrolling back to the top. When clicked it will smooth scroll back to the top & the icon will disappear. The logic behind it can be found [here!](https://freefrontend.com/css-arrows/).
    
    - **Navbar shrinking -** When a user scrolls 50 pixels down from the top of any page, the user will notice that the logo will shrink in size and the background of the navbar be sticky and have a dark background, this is to make sure it doesn't take up too much space & so it can still be seen by the user.

    - **Product Images -** When a user has clicked on an individual product page, they will be presented with an image slider which will allow the user to select an image if there is more than one image. Also, if a user hovers over the image that has been selected, it will zoom in on the picture allowing them to get a better look at the product.

    - **Product Tabs -** When a user has clicked on an individual product page, they will be presented with a tab section where they can view a brief description of the product, a specifications section & a dimensions section.

    - **Order History Accordion -** After a user has placed a successful order, an Order History will appear in the user profile allowing the user to be able to see the date & time the order was placed. If a user clicks one of the headings in the accordion, they can see what items were purchased with quantity, price, line total & total.

     - **Payment Progress Bar -** A user will notice that in the cart, checkout & successful payment pages, when an item is in the basket, a progress bar will appear at the top which will highlight '1' when on the cart page, '2' when on the checkout page & '3' when a successful order has been made. This has been added so that the user has a good understanding of the steps it takes to go from start to finish in placing an order.


### Wireframes

Wireframes were made using [Balsamiq](https://balsamiq.com/) for a clean looking design layout.

- #### Desktop Wireframes

    - [Home Page 1 - Desktop Display](https://i.ibb.co/vHdd0Zt/desktop-home-page-1.png)
    - [Home Page 2 - Desktop Display](https://i.ibb.co/w03kDsX/desktop-home-page-2.png)
    - [Product Page 1 - Desktop Display](https://i.ibb.co/BfQvKL1/desktop-product-page-1.png)
    - [Product Page 2 - Desktop Display](https://i.ibb.co/N3N3RjC/desktop-product-page-2.png)
    - [Individual Product Page 1 - Desktop Display](https://i.ibb.co/9NVrCNB/desktop-individual-product-page-1.png)
    - [Login Page 1 - Desktop Display](https://i.ibb.co/93VTTBk/desktop-login-page-1.png)
    - [Registration Page 1 - Desktop Display](https://i.ibb.co/yQDHxQ0/desktop-register-page-1.png)
    - [Password Reset Page 1 - Desktop Display](https://i.ibb.co/sCC7TDf/desktop-password-reset-page-1.png)
    - [Cart Page 1 - Desktop Display](https://i.ibb.co/Zg1qJg9/desktop-cart-page-1.png)
    - [Checkout Page 1 - Desktop Display](https://i.ibb.co/k1QGwm7/desktop-checkout-page-1.png)
    - [Checkout Page 2 - Desktop Display](https://i.ibb.co/jbNyCZf/desktop-checkout-page-2.png)
    - [Successful Payment Page Page 1 - Desktop Display](https://i.ibb.co/Sc1bGh7/desktop-successful-payment-page-1.png)
    - [Profile Page 1 - Desktop Display](https://i.ibb.co/VVkMhc2/desktop-profile-page-1.png)
    - [Profile Page 2 - Desktop Display](https://i.ibb.co/kK7Jhph/desktop-profile-page-2.png)

- #### Tablet Wireframes

    - [Home Page 1 - Tablet Display](https://i.ibb.co/JxVxs4f/tablet-home-page-1.png)
    - [Home Page 2 - Tablet Display](https://i.ibb.co/Wchr1zK/tablet-home-page-2.png)
    - [Home Page (Side Drawer open) - Tablet Display](https://i.ibb.co/hFYVJtk/tablet-home-page-1-side-drawer-open.png)  
    - [Product Page 1 - Tablet Display](https://i.ibb.co/t239fvj/tablet-product-page-1.png)
    - [Product Page 2 - Tablet Display](https://i.ibb.co/T1hwvXJ/tablet-product-page-2.png)
    - [Individual Product Page 1 - Tablet Display](https://i.ibb.co/YbLcrfF/tablet-individual-product-page-1.png)
    - [Login Page 1 - Tablet Display](https://i.ibb.co/2cbFkLc/tablet-login-page-1.png)
    - [Registration Page 1 - Tablet Display](https://i.ibb.co/ykXn6SS/tablet-register-page-1.png)
    - [Password Reset Page 1 - Tablet Display](https://i.ibb.co/5KzSG7x/tablet-password-reset-page-1.png)
    - [Cart Page 1 - Tablet Display](https://i.ibb.co/qkgRY0v/tablet-cart-page-1.png)
    - [Checkout Page 1 - Tablet Display](https://i.ibb.co/brCqBnS/tablet-checkout-page-1.png)
    - [Checkout Page 2 - Tablet Display](https://i.ibb.co/vw6Ysnw/tablet-checkout-page-2.png)
    - [Successful Payment Page Page 1 - Tablet Display](https://i.ibb.co/G0ThhVm/tablet-successful-payment-page-1.png)
    - [Profile Page 1 - Tablet Display](https://i.ibb.co/Xk1Yx1Y/tablet-profile-page-1.png)
    - [Profile Page 2 - Tablet Display](https://i.ibb.co/ZdMLHDS/tablet-profile-page-2.png)
 
- #### Mobile Wireframes

    - [Home Page 1 - Mobile Display](https://i.ibb.co/L8NwLzR/mobile-home-page-1.png)
    - [Home Page 2 - Mobile Display](https://i.ibb.co/ZWy7bvd/mobile-home-page-2.png)
    - [Home Page (Side Drawer open) - Mobile Display](https://i.ibb.co/ZG2fdXk/mobile-home-page-1-side-drawer-open.png)  
    - [Product Page 1 - Mobile Display](https://i.ibb.co/QNWLTyj/mobile-product-page-1.png)
    - [Product Page 2 - Mobile Display](https://i.ibb.co/stFD0L5/mobile-product-page-2.png)
    - [Individual Product Page 1 - Mobile Display](https://i.ibb.co/Vvf0wrK/mobile-individual-product-page-1.png)
    - [Login Page 1 - Mobile Display](https://i.ibb.co/mHDhGSv/mobile-login-page-1.png)
    - [Registration Page 1 - Mobile Display](https://i.ibb.co/jV5NkRK/mobile-register-page-1.png)
    - [Password Reset Page 1 - Mobile Display](https://i.ibb.co/HPHNy2m/mobile-password-reset-page-1.png)
    - [Cart Page 1 - Mobile Display](https://i.ibb.co/TT6cFkj/mobile-cart-page-1.png)
    - [Checkout Page 1 - Mobile Display](https://i.ibb.co/j8vj0d4/mobile-checkout-page-1.png)
    - [Checkout Page 2 - Mobile Display](https://i.ibb.co/HNYjzV3/mobile-checkout-page-2.png)
    - [Successful Payment Page Page 1 - Mobile Display](https://i.ibb.co/q9NKb7n/mobile-successful-payment-page-1.png)
    - [Profile Page 1 - Mobile Display](https://i.ibb.co/ysMKJBQ/mobile-profile-page-1.png)
    - [Profile Page 2 - Mobile Display](https://i.ibb.co/CbsBxm2/mobile-profile-page-2.png)

### Developer and Business Purpose

- Should be prepared for any double click, fast clicking or clicking different parts of the website.
Every feature must react to it's intended purpose.

- Must show clear & professional examples of HTML, CSS, JavaScript, jQuery & Python.

- Must show a good use of Django knowledge.

- A great example project to put as part of a portfolio.


## Features
 
### Existing Features


#### Navbar:

<div align="center">
    <img src="https://i.ibb.co/ysgyfs3/cts-housewares-navbar.png" alt="CT's Housewares navbar for desktop" aria-label="CT's Housewares navbar for desktop" />
</div>

- The navbar is featured on every page of the website which has been made sticky so that when you scroll down the page, it will not disappear, also when scrolled down more than 50px from the top of the page, the navbar logo will lose the CT's Housewares text & shrink in size, this is so that it's not taking up too much room at the top of the page.


- **Desktop** In the top left-hand corner, a "CT's Housewares logo has been added which will navigate you back to the home page when clicked.

- In the centre on the left, there is a dropdown of product. The options you can pick from are to view all of the products & to view particular brands of your choice.

- In the centre on the right, there is a search bar which will link you to the products & use the search filter to filter products due to the keyword that was entered, it will query the search for words found in the item number, brand, description & about.

- On the right hand, you will find cart which will navigate you to the cart. Also when there is a product in the cart, a red circle will appear just above & to the left of the link to notify how many products are in the cart. This will how many 'products' there are & not the total amount of quantity.

- Also on the right-hand side, you will the 'login' link & the 'register' link. You can click each one of those which will take you to their respective page.

- When a user is logged in, instead of there being 'login' & 'register', you will see 'profile' & 'logout'. Clicking the link will navigate you to their respective page.


<div align="center">
    <img src="https://i.ibb.co/PGc9F8M/cts-housewares-navbar-mobile.png" alt="CT's Housewares navbar for tablet & mobile" aria-label="CT's Housewares navbar for tablet & mobile" />
</div>

- **Tablet & Mobile** In the top left hand corner, a "CT's Housewares logo has been added which will navigate you back to the home page when clicked.

- In the top right hand corner, a burger icon is shown which when clicked will animate into a close symbol & slide out a side drawer, It will also create a darkened overlay on the rest of the page & when clicked, it will slide the side drawer closed again. The links found in the side drawer are the same which are seen in the desktop nabvar.


#### Footer:

<div align="center">
    <img src="https://i.ibb.co/Q6YLXX7/cts-housewares-footer.png" alt="CT's Housewares footer for desktop" aria-label="CT's Housewares footer for desktop" />
</div>

- The navbar is featured on every page & have 2 section, the first section is to give the use a breif overview of what the website is, how it works & what you expect to find when browsing through.

- The second section a list of the product brand which will link you to their respective brand.


#### Up Arrow:

<div align="center">
    <img src="https://i.ibb.co/3RHXVMx/cts-housewares-up-arrow.png" alt="CT's Housewares up arrow" aria-label="CT's Housewares up arrow" />
</div>

- The up arrow will appear in the bottom left-hand corner when you scroll 50px from the top of the page. When hovered over, the icon will do a 360° rotation & change colour to blue. When clicked, you will taken back to the top of the page with a smooth scrolling effect.


#### Home Page:

- **Brand Carousel** - The first thing you are presented with on the home page is a brand carousel where you will find banners with brands you can view throughout the website. These are responsive & will change size due to one device they are viewed on. Carousel autoplays after a set time but you can flick from left to right to view different brands. Each image is also clickable & will take you to that partilcular brand's products when clicked on.

- **Brief Statement** - Underneath the carousel, you will find a brief statement which is essencially a sales pitch letting you know what you are going to find when browsing throughout the website.


#### Product Page:

- **Brand Selector** - At the top of the brands page, you have the option to select a brand from the select dropdown, simply choose which brand you'd like to view & click "Go!".

- **Pagination** - - Pagination has been included in the products page to keep data cleaner & to limit the amount of data shown at one time, this can help quite substantially with loading time if there are lots of products. Simply flick from page to page to view more products. When a new brand or search query has been made, you still begin at page 1. If a user is on page 1, the first & previous buttons will not be visible & if the user is on the last page, the next & last buttons will not be visible. Also, the current page has been coloured blue to signify which page the user is on.

- **Product Cards** - Each product has it's own card which will consist of an image of the product, product description, price & the option to add to cart. If a product is out of stock, instead of there being add to cart, there will be item out of stock.

- **Quick Add to Cart** - Add to cart has been added to each of the cards to speed up the process of adding to cart. You also have a quantity selector which will go as high as the quantity in stock. If a user was the add a product to the cart which was already in the cart, it will simply add the number you add to the number of items already in the cart of that product. You cannot add more than the stock quantity to the basket & if the items you add to the cart + the amount of items you already have in your cart of that particular item comes to more than the overall quantity of that item, you will get notified that you can not add that may items to the cart.

