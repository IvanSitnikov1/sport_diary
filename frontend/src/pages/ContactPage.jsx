import {Form, Button, Container} from 'react-bootstrap';


export const ContactPage = () => {
    return (
        <>
            <Container style={{width: '700px'}}>
                <h1 className="text-center"> Связаться с нами </h1>
                <Form>
                    <Form.Group controlId="formBasicEmail">
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="Введите email" />
                        <Form.Text>
                            We'll never share your email with anyone else
                        </Form.Text>
                    </Form.Group>
                    <Form.Group controlId="formBasicPassword">
                        <Form.Label>Example textarea</Form.Label>
                        <Form.Control as="textarea" rows="5" placeholder="Введите сообщение" />
                    </Form.Group>
                    <Form.Group controlId="formBasicCheckbox">
                        <Form.Check type="checkbox" label="Check me out" />
                    </Form.Group>
                    <Button variant="primary" type="submit" className="mt-2">Отправить</Button>
                </Form>
            </Container>
        </>
    );
};
