var b=(w,r,o)=>new Promise((p,t)=>{var c=a=>{try{i(o.next(a))}catch(n){t(n)}},u=a=>{try{i(o.throw(a))}catch(n){t(n)}},i=a=>a.done?p(a.value):Promise.resolve(a.value).then(c,u);i((o=o.apply(w,r)).next())});import{r as f,a as k,u as A,c as N,b as g,d as s,w as B,e as x,v as y,t as F,f as C,g as L,h as O,i as z,_ as T,j as _,k as Y,l as H,m as Z,o as h,n as E}from"./index-D6OADOrS.js";const W={class:"min-h-screen bg-[#EDE8E5] relative overflow-hidden"},G={class:"max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col lg:flex-row min-h-screen"},R={class:"w-full lg:w-1/2 flex items-center justify-center lg:justify-start relative z-10 py-12 lg:py-0"},V={class:"w-full max-w-md bg-white rounded-lg shadow-md p-8"},I={key:0,class:"text-red-500 text-sm mt-1"},P={key:0,class:"text-red-500 text-sm mt-1"},U={class:"flex justify-end"},D=["disabled"],q={__name:"Login",setup(w){const r=f(""),o=f(""),p=f(null),t=k({email:"",password:""});_("$call");const c=_("$auth"),u=Y(),i=H(),a=A(),n=l=>/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(l),m=l=>{switch(t[l]="",l){case"email":r.value?n(r.value)||(t.email="Invalid email format"):t.email="Email is required";break;case"password":o.value?o.value.length<6&&(t.password="Password must be at least 6 characters long"):t.password="Password is required";break}},v=N(()=>r.value&&o.value&&!t.email&&!t.password),M=()=>b(this,null,function*(){if(m("email"),m("password"),v.value)try{(yield c.login(r.value,o.value))&&(a.success("Login successful!",{position:"top-right",timeout:5e3,closeOnClick:!0,pauseOnFocusLoss:!0,pauseOnHover:!0,draggable:!0,draggablePercent:.6,showCloseButtonOnHover:!1,hideProgressBar:!0,closeButton:"button",icon:!0,rtl:!1}),u.push({name:"Home"}))}catch(l){a.error("Login failed. Please check your credentials and try again.",{position:"top-right",timeout:5e3,closeOnClick:!0,pauseOnFocusLoss:!0,pauseOnHover:!0,draggable:!0,draggablePercent:.6,showCloseButtonOnHover:!1,hideProgressBar:!0,closeButton:"button",icon:!0,rtl:!1})}});return i.query.route&&(p.value=i.query.route,u.replace({query:null})),(l,e)=>{const j=Z("router-link");return h(),g("div",W,[s("div",G,[s("div",R,[s("div",V,[e[7]||(e[7]=s("h2",{class:"text-center font-semibold font-sans text-[#212529] mb-10 sm:mb-2"}," Welcome to British Asian Trust Portal ",-1)),e[8]||(e[8]=s("p",{class:"text-center text-[#212529] mb-6"}," Login to access your dashboard, complete surveys, earn points, and get personalized recommendations to support your wellness. ",-1)),s("form",{onSubmit:B(M,["prevent"]),class:"space-y-4"},[s("div",null,[e[4]||(e[4]=s("label",{for:"email",class:"block mb-1"},"Email",-1)),x(s("input",{type:"email",id:"email","onUpdate:modelValue":e[0]||(e[0]=d=>r.value=d),onInput:e[1]||(e[1]=d=>m("email")),class:"mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm",placeholder:"Enter your email address"},null,544),[[y,r.value]]),t.email?(h(),g("p",I,F(t.email),1)):C("",!0)]),s("div",null,[e[5]||(e[5]=s("label",{for:"password",class:"block mb-1"},"Password",-1)),x(s("input",{type:"password",id:"password","onUpdate:modelValue":e[2]||(e[2]=d=>o.value=d),onInput:e[3]||(e[3]=d=>m("password")),class:"mt-1 block w-full border border-gray-300 rounded-md shadow-sm py-2 px-3 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm",placeholder:"Enter your password"},null,544),[[y,o.value]]),t.password?(h(),g("p",P,F(t.password),1)):C("",!0)]),s("div",U,[L(j,{to:{name:"Forgot"},class:"text-sm text-gray-600 hover:text-gray-900"},{default:O(()=>e[6]||(e[6]=[E("Forgot Password?")])),_:1})]),s("div",null,[s("button",{type:"submit",disabled:!v.value,class:"w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-[#CA2247] hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 disabled:opacity-50 disabled:cursor-not-allowed"}," LOGIN ",8,D)])],32),e[9]||(e[9]=z('<div class="mt-4 space-y-3"><a href="https://accounts.google.com/o/oauth2/auth?redirect_uri=https%3A%2F%2Fbtasian.suvaidyam.com%2Fapi%2Fmethod%2Fbritish_asian_trust.api.my_login_via_google&amp;state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiMjg1YjVhYmQ1YTY2Y2RiNGU3NTZkZmFmNmZiNWNhODc0ZDI3ZTY4M2U3NzU4NTQwZTgwMmRmZjkiLCAicmVkaXJlY3RfdG8iOiAiL2FwcC9idWlsZCJ9&amp;scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&amp;response_type=code&amp;client_id=720319117261-1kuhqoutuq2j8ud0b8dsp1oen4glmruq.apps.googleusercontent.com" class="w-full flex justify-center items-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"><svg class="w-5 h-5 mr-2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"></path><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"></path><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"></path><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"></path></svg> Login with Google </a><a href="https://login.live.com/oauth20_authorize.srf?client_id=c28ed05b-846a-414e-b8df-bbb602316b22&amp;scope=openid+email+profile&amp;redirect_uri=https%3a%2f%2fbtasian.suvaidyam.com%2fapi%2fmethod%2fbritish_asian_trust.api.my_login_via_office_365&amp;response_type=code&amp;state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiMWI3NDEzMmI1YTcyMDVhYTU1ZjI2YWRjMTFhNWE5MTRmOTM5ZGFkYzY4YmMzYWY5N2UwNGUxMmUiLCAicmVkaXJlY3RfdG8iOiAiL2FwcC9idWlsZCJ9&amp;uaid=c35885a2c1184f4186654fd596f46435&amp;msproxy=1&amp;issuer=mso&amp;tenant=common&amp;ui_locales=en-US&amp;epct=PAQABDgEAAADW6jl31mB3T7ugrWTT8pFegkih0W8sUO6f7208OAMBvr0o-aKavF-3Om0wE25w4jAYP5hqO5RXvSW79U28PDQSXMLHLVx0xZYuSXwNaXchMROxYyOQk0ID90pm3JYjsRXrZNGuiLsTJKVp3mFaGz4imNGEWNK5svN-r16x1-J1H1a6dvTZxo6BrUXhlHars8gJjOiC58aWZ2fklaBEGrfXKKlEqYueMJE56Ed_-nT_aSAA&amp;jshs=-1&amp;jsh=&amp;jshp=" class="w-full flex justify-center items-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"><svg class="w-5 h-5 mr-2" viewBox="0 0 23 23" xmlns="http://www.w3.org/2000/svg"><path fill="#f3f3f3" d="M0 0h23v23H0z"></path><path fill="#f35325" d="M1 1h10v10H1z"></path><path fill="#81bc06" d="M12 1h10v10H12z"></path><path fill="#05a6f0" d="M1 12h10v10H1z"></path><path fill="#ffba08" d="M12 12h10v10H12z"></path></svg> Login with Microsoft </a></div>',1))])]),e[10]||(e[10]=s("div",{class:"hidden lg:block lg:w-1/2 relative"},[s("svg",{class:"absolute right-0 bottom-0 w-[300px] h-[300px] lg:w-[700px] lg:h-[600px]",viewBox:"0 0 719 681",fill:"none",xmlns:"http://www.w3.org/2000/svg"},[s("path",{"fill-rule":"evenodd","clip-rule":"evenodd",d:"M10.6721 358.09C43.7944 290.528 148.486 299.88 203.921 248.991C237.118 218.516 233.243 164.646 260.492 128.755C298.361 78.8762 330.329 2.09349 392.93 0.0381908C454.772 -1.99227 485.461 77.4593 530.486 119.891C565.441 152.832 598.797 184.384 628.553 222.085C662.81 265.488 725.275 303.219 718.489 358.09C711.449 415.017 625.945 426.357 597.155 475.972C568.46 525.423 606.218 613.235 555.318 639.29C503.188 665.974 451.086 573.596 392.93 580.511C321.677 588.984 278.12 686.509 206.596 680.755C139.575 675.363 89.6252 610.766 54.7335 553.303C19.5091 495.292 -19.2021 419.028 10.6721 358.09Z",fill:"#DBB729"})]),s("img",{src:T,alt:"Two women in traditional attire",class:"absolute inset-0 w-full h-full object-cover"})],-1))])])}}};export{q as default};
