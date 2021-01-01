module.exports = async function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    context.log( 'HERE ')
    for (var key in req.body) {
        if (req.body.hasOwnProperty(key)) {
            let value = req.body[key];
            context.log( `value for KEY:${key} is VALUE:${value}` )
            if (key=="payload_fields") {
                context.log('PAYLOAD FIELDS');
                context.log(JSON.stringify(value))
            }
        }
    }

    context.bindings.httpDocument = req.body;

    const name = (req.query.name || (req.body && req.body.name));
    const responseMessage = name
        ? "Hello, " + name + ". This HTTP triggered function executed successfully."
        : "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.";

    context.res = {
        // status: 200, /* Defaults to 200 */
        body: responseMessage
    };
}