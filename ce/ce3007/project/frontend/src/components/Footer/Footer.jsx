import React from 'react';
import './Footer.scss';

export default function Footer() {
    return (
        <footer className="Footer">
            {/* <br /> */}
            <h5 className='copyright'>
                © 2023 Copyright:&nbsp;
                <a href="https://1chooo-github-io.vercel.app/" target="_blank">
                    Hugo ChunHo Lin 👨🏻‍💻
                </a>
            </h5>
            <div className='icon'>
                <p align="center">
                    <a href="https://github.com/1chooo" target="_blank">
                        <img src="https://skillicons.dev/icons?i=github" />
                    </a>
                    <a href="https://www.linkedin.com/in/1chooo/" target="_blank">
                        <img src="https://skillicons.dev/icons?i=linkedin" />
                    </a>
                    <a href="https://awseducate.tw/2" target="_blank">
                        <img src="https://skillicons.dev/icons?i=aws" />
                    </a>
                    <a href="https://www.instagram.com/lcho____/" target="_blank">
                        <img src="https://skillicons.dev/icons?i=instagram" />
                    </a>
                    <a href="https://www.instagram.com/lcho____/" target="_blank">
                        <img src="https://skillicons.dev/icons?i=twitter" />
                    </a>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                </p>
            </div>
        </footer>
    );
}
