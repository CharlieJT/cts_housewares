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

- #### Tablet Wireframes


 
- #### Mobile Wireframes
