var _=(b,a,s)=>new Promise((d,p)=>{var n=i=>{try{u(s.next(i))}catch(r){p(r)}},o=i=>{try{u(s.throw(i))}catch(r){p(r)}},u=i=>i.done?d(i.value):Promise.resolve(i.value).then(n,o);u((s=s.apply(b,a)).next())});import{r as m,a as H,u as I,c as T,b as f,d as t,e as v,_ as V,w as O,f as j,v as R,t as A,g as z,h as q,i as M,j as B,k as w,l as C,m as G,n as P,o as S,p as W,q as g,N as E,L as J}from"./index-CpASjXB_.js";const U={class:"min-h-screen bg-white"},Q={class:"max-w-[1920px] mx-auto relative"},X={class:"relative flex flex-col lg:flex-row justify-center min-h-screen bg-gray-100"},$={class:"lg:w-1/2 p-4 sm:p-8 flex flex-col justify-center items-center bg-white shadow-xl"},K={class:"w-full max-w-lg"},ee={key:0,class:"text-red-500 text-xs sm:text-sm mt-1"},te={class:"relative"},oe=["type"],se={key:0,class:"text-red-500 text-xs sm:text-sm mt-1"},ae={class:"flex justify-end mb-2"},ie=["disabled"],le={key:0},ne={key:1,class:"flex items-center"},re={class:"mt-4 text-center"},de="https://accounts.google.com/o/oauth2/auth?redirect_uri=https%3A%2F%2Fbtasian.suvaidyam.com%2Fapi%2Fmethod%2Fbritish_asian_trust.api.my_login_via_google&state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiMjg1YjVhYmQ1YTY2Y2RiNGU3NTZkZmFmNmZiNWNhODc0ZDI3ZTY4M2U3NzU4NTQwZTgwMmRmZjkiLCAicmVkaXJlY3RfdG8iOiAiL2FwcC9idWlsZCJ9&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email&response_type=code&client_id=720319117261-1kuhqoutuq2j8ud0b8dsp1oen4glmruq.apps.googleusercontent.com",pe="https://login.microsoftonline.com/common/oauth2/v2.0/authorize?redirect_uri=https%3a%2f%2fbtasian.suvaidyam.com%2fapi%2fmethod%2fbritish_asian_trust.api.my_login_via_office_365&state=eyJzaXRlIjogImh0dHA6Ly9idGFzaWFuLnN1dmFpZHlhbS5jb20iLCAidG9rZW4iOiAiYTIwNTJlY2YzODIzMDI5NTQ2NThjMjY2ZDliOGI3ZWYwYTAwYjJhMjYxODFjYzQ0YmFkNjQ1YjMiLCAicmVkaXJlY3RfdG8iOiAiL2FwcCJ9&response_type=code&scope=openid+email+profile&client_id=c28ed05b-846a-414e-b8df-bbb602316b22&sso_nonce=AwABEgEAAAADAOz_BQD0_6Ar8NwBdlHYKzVYmVX60SYWmU33iETSyQ_ougU6j_1JG37adzZ-SO-HreW8x9QnR79ZfuhZMek433986gCjxYcgAA&client-request-id=bceba0a3-5344-4ea6-a171-a8c06b638a9a&mscrid=bceba0a3-5344-4ea6-a171-a8c06b638a9a",me={__name:"Login",setup(b){const a=m(""),s=m(""),d=m(!1),p=m(null),n=m(!1),o=H({email:"",password:""}),u=G("$auth"),i=P(),r=S(),y=I(),k=["gmail.com","outlook.com","hotmail.com","yahoo.com","aol.com","mail.com","protonmail.com","icloud.com"],Y=l=>{if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(l))return!1;const h=l.split("@")[1].toLowerCase();return!k.includes(h)},x=l=>{switch(o[l]="",l){case"email":if(!a.value)o.email="Email is required";else if(!Y(a.value))if(a.value.includes("@")){const e=a.value.split("@")[1].toLowerCase();k.includes(e)?o.email="Please use your business email address":o.email="Invalid email format"}else o.email="Invalid email format";break;case"password":s.value?s.value.length<6&&(o.password="Password must be at least 6 characters long"):o.password="Password is required";break}},F=T(()=>a.value&&s.value&&!o.email&&!o.password),D=()=>_(this,null,function*(){if(x("email"),x("password"),F.value)try{n.value=!0,(yield u.login(a.value,s.value))&&(y.success("Login successful!",{position:"top-right",timeout:5e3}),i.push(p.value||{name:"Home"}))}catch(l){y.error("Login failed. Please check your credentials and try again.",{position:"top-right",timeout:5e3})}finally{n.value=!1}}),L=()=>{d.value=!d.value},N=()=>{window.location.href=de},Z=()=>{window.location.href=pe};return r.query.route&&(p.value=r.query.route,i.replace({query:null})),(l,e)=>{const h=W("router-link");return g(),f("div",U,[t("div",Q,[v(E),t("div",X,[e[15]||(e[15]=t("div",{class:"lg:w-1/2 h-64 lg:h-auto"},[t("img",{src:V,alt:"Family using laptop",class:"object-cover w-full h-full"})],-1)),t("div",$,[t("div",K,[e[12]||(e[12]=t("h1",{class:"font-poppins text-[24px] font-semibold leading-[28px] lg:text-[34px] lg:leading-[37.4px] text-[#0D4688] mb-4 sm:mb-6 text-center"}," Welcome to Outcome Readiness ",-1)),e[13]||(e[13]=t("p",{class:"font-poppins text-[14px] font-normal leading-[18.34px] tracking-[0.0025em] text-[#2F2F2F] lg:text-[14px] lg:leading-[18.34px] mb-6 sm:mb-8 text-center"}," Login to empower your organization and gain access to surveys, personalized recommendations, and tools to drive impact. ",-1)),t("form",{onSubmit:O(D,["prevent"]),class:"space-y-4"},[t("div",null,[e[4]||(e[4]=t("label",{for:"email",class:"sr-only"},"Email ID",-1)),j(t("input",{id:"email","onUpdate:modelValue":e[0]||(e[0]=c=>a.value=c),type:"email",required:"",class:"w-full px-4 h-12 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]",placeholder:"Email ID",onInput:e[1]||(e[1]=c=>x("email"))},null,544),[[R,a.value]]),o.email?(g(),f("p",ee,A(o.email),1)):z("",!0)]),t("div",te,[e[6]||(e[6]=t("label",{for:"password",class:"sr-only"},"Password",-1)),j(t("input",{id:"password","onUpdate:modelValue":e[2]||(e[2]=c=>s.value=c),type:d.value?"text":"password",required:"",class:"w-full px-4 h-12 border border-gray-300 rounded-md font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#2F2F2F] focus:outline-none focus:ring-2 focus:ring-[#0D4688] focus:border-[#0D4688]",placeholder:"Password",onInput:e[3]||(e[3]=c=>x("password"))},null,40,oe),[[q,s.value]]),t("button",{type:"button",onClick:L,class:"absolute inset-y-0 right-0 pr-3 flex items-center","aria-label":"Toggle password visibility"},e[5]||(e[5]=[t("svg",{class:"h-5 w-5 text-gray-400",fill:"none",stroke:"currentColor",viewBox:"0 0 24 24",xmlns:"http://www.w3.org/2000/svg"},[t("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M15 12a3 3 0 11-6 0 3 3 0 016 0z"}),t("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"})],-1)])),o.password?(g(),f("p",se,A(o.password),1)):z("",!0)]),t("div",ae,[v(h,{to:"/forgot",class:"font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#0D4688] hover:underline"},{default:M(()=>e[7]||(e[7]=[w(" Forgot Password? ")])),_:1})]),t("button",{type:"submit",disabled:!F.value||n.value,class:"w-full bg-orange-500 text-white h-12 px-4 rounded-full hover:bg-orange-600 transition duration-300 disabled:opacity-50 disabled:cursor-not-allowed font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] flex items-center justify-center"},[n.value?(g(),f("span",ne,[v(B(J),{class:"animate-spin -ml-1 mr-3 h-5 w-5 text-white"}),e[8]||(e[8]=w(" Processing... "))])):(g(),f("span",le,"LOGIN"))],8,ie)],32),t("div",re,[v(h,{to:"/register",class:"font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left text-[#0D4688] hover:underline"},{default:M(()=>e[9]||(e[9]=[w(" Don't have an account? Sign up ")])),_:1})]),e[14]||(e[14]=t("div",{class:"mt-6 flex items-center"},[t("div",{class:"flex-grow border-t border-gray-300"}),t("span",{class:"flex-shrink mx-4 text-gray-600 font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left"},"OR"),t("div",{class:"flex-grow border-t border-gray-300"})],-1)),t("div",{class:"mt-6 space-y-2"},[t("button",{onClick:N,class:"w-full border border-gray-300 text-gray-700 h-12 px-4 rounded-full hover:bg-gray-50 transition duration-300 flex items-center justify-center font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left"},e[10]||(e[10]=[C('<svg class="h-5 w-5 mr-2" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"></path><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"></path><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"></path><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"></path><path fill="none" d="M1 1h22v22H1z"></path></svg> Continue with Google ',2)])),t("button",{onClick:Z,class:"w-full border border-gray-300 text-gray-700 h-12 px-4 rounded-full hover:bg-gray-50 transition duration-300 flex items-center justify-center font-poppins text-[16px] font-normal leading-[20.96px] tracking-[0.0025em] text-left"},e[11]||(e[11]=[C('<svg class="h-5 w-5 mr-2" viewBox="0 0 23 23"><path fill="#f3f3f3" d="M0 0h23v23H0z"></path><path fill="#f35325" d="M1 1h10v10H1z"></path><path fill="#81bc06" d="M12 1h10v10H12z"></path><path fill="#05a6f0" d="M1 12h10v10H1z"></path><path fill="#ffba08" d="M12 12h10v10H12z"></path></svg> Continue with Microsoft ',2)]))])])])])])])}}};export{me as default};
