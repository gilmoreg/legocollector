import React from 'react';
import './Login.css';

const amazonLogin = () => {
  window.amazon.Login.authorize(
    { scope: 'profile' },
    (response) => {
      console.log(response);
    });
  return false;
};
/*
{
  access_token: "Atza|IwEBIEUOpgBKYnfV0HwxYsUDtyI7c4bkSil0tB9kcsLfbP2C_lbPfKs46A9sLS7JHCWHqA_LxvDHI5qHN6XoWyyiuxWlNo0ylbUUGDM3H8pIwebdF0B4_VKUiKFTKIkHXHyFYPy9xM3e2DAhNTaA2XngLHgXCRhKuaoNMDEn8__EjDO6a6azZGEEMcj-7mNxGujj7HxUj0hkuhAFPY_qBsgUdzKgq2I30tdVosGKHBgxzAvGX9nU0Q7lDFj1YWpS3eH6vnu5MfBRPOibjdssC9joAku4KLEZtVO_2M8E5xVMQ1ehmq5K_LfMvqb3JR9j_J2bd3gcJTI80mi5cbru-zOsID0QGa1v8W3NRPhyXT_3EA1Hce_aWgel-PWVc1tddQldUyw_U-4owwIbIKMDJ8-okquXNed5_JZFqeQTGahXZ9pJN5qEYe64XfPl20tG4HzVEXIFYMVLoriOGLk37V3UdLoePDD9SMSw9Co8nbgaiAn60c-fcbcFGxb_2KK3P12KnoCa8dXUIRUG8UXHZq_-XtMjhw66Xz_n52yNbSHBBOJGO9gVeSg8FzJpOX8V77a4pTw"
  scope:"profile"
  status:"complete"
  token_type:"bearer"
}
So with authorization Grant, I would send this token to the server, which would then
call  https://api.amazon.com/user/profile?access_token=${token}
Should return 
{
    "user_id": "amznl.account.K2LI23KL2LK2",
    "email":"mhashimoto-04@plaxo.com",
    "name" :"Mork Hashimoto",
    "postal_code": "98052"
}
So what do I do with that there? I have an email address basically,
which I wouldn't have if the login info were wrong, right?
Ok so the idea is that I can create a user based on that email address and maybe user_id
That's how I know I have a valid user and which user I am dealing with
From then on I would like to...use JWT so I don't have to mess with AWS every request

So the server side login function:
  1. Asks Amazon about this access token
  2. Gets an email address
  3. Sees if that email exists in the db, if so, returns the user id
     If not, creates that user and returns the id
  4. Signs the user id into a JWT
  5. Returns that and the email (for display purposes) to the user for future requests
The client side can then stash the JWT in localStorage

*/

const Login = () => (
  <button id="LoginWithAmazon" onClick={amazonLogin}>
    <img
      alt="Login with Amazon"
      src="https://images-na.ssl-images-amazon.com/images/G/01/lwa/btnLWA_gold_156x32.png"
      width="156"
      height="32"
    />
  </button>
);

export default Login;
