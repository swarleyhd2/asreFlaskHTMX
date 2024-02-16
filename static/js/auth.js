import { initializeApp } from '/firebase/auth'
import { getAuth, createUserWithEmailAndPassword, signOut, setPersistence} from "firebase/auth"

initializeApp({
    apiKey: "AIzaSyA0v1MRmfM3XWTT5M_OpqP_A6z06vDEm7M",
    authDomain: "allstaterental.firebaseapp.com",
});

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
setPersistence(auth, 'none');

const newUser = (email, password) => {
    console.log('hello world!')
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            userCredential.user.getIdToken().then((token) => {
                const csrfToken = browser.cookies.get({name: "csrfToken"})
                return postToSessionLogin('/sessionLogin', token, csrfToken)
            })
        }).then(() => {
            signOut(auth)
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
        });
}
