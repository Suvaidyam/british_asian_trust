var p=(l,e,i)=>new Promise((d,t)=>{var n=r=>{try{u(i.next(r))}catch(a){t(a)}},o=r=>{try{u(i.throw(r))}catch(a){t(a)}},u=r=>r.done?d(r.value):Promise.resolve(r.value).then(n,o);u((i=i.apply(l,e)).next())});import{_ as f,c as b,a as s,w as g,b as m,v as w,o as x}from"./index-Csu5KMvf.js";const y={data(){return{email:null,password:null}},inject:["$auth"],mounted(){return p(this,null,function*(){var l,e;(e=(l=this.$route)==null?void 0:l.query)!=null&&e.route&&(this.redirect_route=this.$route.query.route,this.$router.replace({query:null}))})},methods:{login(){return p(this,null,function*(){this.email&&this.password&&(yield this.$auth.login(this.email,this.password))&&this.$router.push({name:"Home"})})}}},h={class:"min-h-screen bg-red-200 flex"},v={class:"mx-auto w-full max-w-sm lg:w-96"};function $(l,e,i,d,t,n){return x(),b("div",h,[s("div",v,[s("form",{onSubmit:e[2]||(e[2]=g((...o)=>n.login&&n.login(...o),["prevent"])),class:"space-y-6"},[e[3]||(e[3]=s("label",{for:"email"}," Username: ",-1)),m(s("input",{type:"text","onUpdate:modelValue":e[0]||(e[0]=o=>t.email=o)},null,512),[[w,t.email]]),e[4]||(e[4]=s("br",null,null,-1)),e[5]||(e[5]=s("label",{for:"password"}," Password: ",-1)),m(s("input",{type:"password","onUpdate:modelValue":e[1]||(e[1]=o=>t.password=o)},null,512),[[w,t.password]]),e[6]||(e[6]=s("button",{class:"bg-blue-500 block text-white p-2 hover:bg-blue-700",type:"submit"}," Sign in ",-1))],32)])])}const B=f(y,[["render",$]]);export{B as default};
