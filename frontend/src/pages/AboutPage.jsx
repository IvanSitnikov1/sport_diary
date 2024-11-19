import {Container, Tab, Nav, Row, Col} from 'react-bootstrap';

export const AboutPage = () => {
    return (
        <>
            <Container>
                <Tab.Container id="left-tabs-example" defaultActiveKey="first">
                    <Row>
                        <Col sm={3}>
                            <Nav variant="pills" className="flex-column mt-2">
                                <Nav.Item>
                                    <Nav.Link eventKey="first">First</Nav.Link>
                                </Nav.Item>
                                <Nav.Item>
                                    <Nav.Link eventKey="second">Second</Nav.Link>
                                </Nav.Item>
                                <Nav.Item>
                                    <Nav.Link eventKey="third">Third</Nav.Link>
                                </Nav.Item>
                            </Nav>
                        </Col>
                        <Col sm={9}>
                            <Tab.Content className="mt-2">
                                <Tab.Pane eventKey="first">
                                    <img src="https://itchief.ru/assets/images/covers/bootstrap-4-spacing.png" style={{maxWidth: '100%'}} alt="example" />
                                    <p>
                                        Как это работает. Горизонтальные отступы между столбцами с использованием padding.
                                        Мы устанавливаем padding-right и padding-left для каждого столбца и используем отрицательное
                                        значение margin для смещения в начале и конце каждой строки для выравнивания содержимого.
                                        Начало отступа шириной в 1.5rem (24px). Это позволяет нам сопоставить нашу сетку с масштабом
                                        отступов и интервалов полей. Отступы могут быть быстро отрегулированы. Используйте специфичные
                                        для контрольной точки классы отступов для изменения горизонтальных, вертикальных и сразу всех отступов.
                                    </p>
                                </Tab.Pane>
                                <Tab.Pane eventKey="second">
                                    <img src="https://itchief.ru/assets/images/covers/bootstrap-4-spacing.png" style={{maxWidth: '100%'}} alt="example" />
                                    <p>
                                        Как это работает. Горизонтальные отступы между столбцами с использованием padding.
                                        Мы устанавливаем padding-right и padding-left для каждого столбца и используем отрицательное
                                        значение margin для смещения в начале и конце каждой строки для выравнивания содержимого.
                                        Начало отступа шириной в 1.5rem (24px). Это позволяет нам сопоставить нашу сетку с масштабом
                                        отступов и интервалов полей. Отступы могут быть быстро отрегулированы. Используйте специфичные
                                        для контрольной точки классы отступов для изменения горизонтальных, вертикальных и сразу всех отступов.
                                    </p>
                                </Tab.Pane>
                                <Tab.Pane eventKey="third">
                                    <img src="https://itchief.ru/assets/images/covers/bootstrap-4-spacing.png" style={{maxWidth: '100%'}} alt="example" />
                                    <p>
                                        Как это работает. Горизонтальные отступы между столбцами с использованием padding.
                                        Мы устанавливаем padding-right и padding-left для каждого столбца и используем отрицательное
                                        значение margin для смещения в начале и конце каждой строки для выравнивания содержимого.
                                        Начало отступа шириной в 1.5rem (24px). Это позволяет нам сопоставить нашу сетку с масштабом
                                        отступов и интервалов полей. Отступы могут быть быстро отрегулированы. Используйте специфичные
                                        для контрольной точки классы отступов для изменения горизонтальных, вертикальных и сразу всех отступов.
                                    </p>
                                </Tab.Pane>
                            </Tab.Content>
                        </Col>
                    </Row>
                </Tab.Container>
            </Container>
        </>
    );
};
