import Building from './5-building'

export default class SkyHighBuilding extends Building {
    constructor(sqtf, floors) {
        super(sqtf);
        this._floors = floors;
    }

    get sqtf() {
        return  this._sqtf;
    }

    get floors() {
        return this._floors;
    }

    evacuationWarningMessage() {
        return `Evacuate slowly the ${this._floors} floors`;
    }
}
