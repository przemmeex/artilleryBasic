import { testCatPage, testDogPage } from '../commands/login';

export async function artilleryScript(page: any, vuContext: any, events: any, test: any) {
    const {step} = test;
    await testDogPage(page, step);
    events.emit('counter',`@@@ message for emit`,1);
    await testCatPage(page, step);
}