import React from 'react';
import './Login.css';

// TODO move to config/env
const API_URL = 'http://localhost:5000';

const fetchProfile = accessToken =>
  fetch(`${API_URL}/login`,
    { method: 'POST',
      body: JSON.stringify({ access_token: accessToken }),
    })
    .then(res => res.json())
    .then(res => console.log(res));

const amazonLogin = () =>
  window.amazon.Login.authorize({ scope: 'profile' },
    response => fetchProfile(response.access_token));

export default () => (
  <button id="LoginWithAmazon" onClick={amazonLogin}>
    <img
      alt="Login with Amazon"
      src="https://images-na.ssl-images-amazon.com/images/G/01/lwa/btnLWA_gold_156x32.png"
      width="156"
      height="32"
    />
  </button>
);

/*
{
  access_token: "Atza|IwEBIEUOpgBKYnfV0HwxYsUDtyI7c4bkSil0tB9kcsLfbP2C_lbPfKs46A9sLS7JHCWHqA_LxvDHI5qHN6XoWyyiuxWlNo0ylbUUGDM3H8pIwebdF0B4_VKUiKFTKIkHXHyFYPy9xM3e2DAhNTaA2XngLHgXCRhKuaoNMDEn8__EjDO6a6azZGEEMcj-7mNxGujj7HxUj0hkuhAFPY_qBsgUdzKgq2I30tdVosGKHBgxzAvGX9nU0Q7lDFj1YWpS3eH6vnu5MfBRPOibjdssC9joAku4KLEZtVO_2M8E5xVMQ1ehmq5K_LfMvqb3JR9j_J2bd3gcJTI80mi5cbru-zOsID0QGa1v8W3NRPhyXT_3EA1Hce_aWgel-PWVc1tddQldUyw_U-4owwIbIKMDJ8-okquXNed5_JZFqeQTGahXZ9pJN5qEYe64XfPl20tG4HzVEXIFYMVLoriOGLk37V3UdLoePDD9SMSw9Co8nbgaiAn60c-fcbcFGxb_2KK3P12KnoCa8dXUIRUG8UXHZq_-XtMjhw66Xz_n52yNbSHBBOJGO9gVeSg8FzJpOX8V77a4pTw"
  scope:"profile"
  status:"complete"
  token_type:"bearer"
}
So with authorization Grant, I would send this token to the server, which would then

*/
